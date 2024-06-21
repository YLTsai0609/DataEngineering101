import json
import numpy as np
import pandas as pd
import json
import boto3
import dateutil.tz
import datetime
import os

def handler(event, context):
    s3 = boto3.client('s3')
    data_bucket = os.environ['data_bucket']
    csv_file = s3.get_object(
        Bucket=data_bucket,
        Key='dataset/merged_data.csv'
        )
    
    data = pd.read_csv(csv_file['Body'])
    user_ids = data['user_id'].unique()
    item_ids = data.groupby('item_id').size().sort_values(ascending=False).index.to_numpy()
    
    user_to_index = {user_id: index for index, user_id in enumerate(user_ids)}
    item_to_index = {item_id: index for index, item_id in enumerate(item_ids)}
    
    user_id = int(event['userId'])
    user_idx = user_to_index[user_id]
    item_idx_list = np.array([item_to_index[item_id] for item_id in item_ids])
    user_input = np.full(len(item_ids), user_idx).reshape(-1, 1)
    item_input = item_idx_list.reshape(-1, 1)
    
    sagemaker_client = boto3.client('sagemaker-runtime')
    response = sagemaker_client.invoke_endpoint(
        EndpointName='ncf-model-endpoint',
        ContentType='application/json',
        Body=json.dumps(
            {"user_input": user_input.tolist(),
            "item_input": item_input.tolist()}
        )
    )
    
    predictions = json.loads(response['Body'].read().decode('utf-8'))
    predictions_array = np.array(predictions['predictions']).reshape(-1)
    top_10_indices = np.argsort(predictions_array)[-10:][::-1]
    top_10_item_ids = [item_ids[idx] for idx in top_10_indices]
    
    csv_file = s3.get_object(
        Bucket=data_bucket,
        Key='dataset/training_item.csv'
        )
    items_df = pd.read_csv(csv_file['Body'])
    df = pd.DataFrame(data={'ITEM_ID':top_10_item_ids})
    items_list = df.merge(items_df)
    items_list_to_store = items_list.to_csv()
    items_list['model'] = 'sagemaker'
    
    # S3 에 추천 결과 저장
    s3 = boto3.client('s3')
    bucket_name = os.environ['bucket_name']
    
    apnortheast2 = dateutil.tz.gettz('Asia/Seoul')
    prefix= "recommended-list/" + datetime.datetime.now(tz=apnortheast2).strftime("%Y-%m-%d-%H") + "/"
    key_name = 'sagemaker - userId: ' + str(user_id) + '.csv'
    s3.put_object(Bucket=bucket_name, Key=prefix+key_name, Body=items_list_to_store)

    return {
        'statusCode': 200,
        'body': items_list.to_json()
    }
