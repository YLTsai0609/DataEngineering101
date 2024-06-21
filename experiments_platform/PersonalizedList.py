import json
import boto3
import datetime
import time
import pandas as pd
import dateutil.tz
import os

def handler(event, context):
    personalize = boto3.client('personalize')
    personalize_runtime = boto3.client('personalize-runtime')

    user_id = str(event['userId'])
    base_campaign_arn = os.environ['campaign_arn']
    
    get_recommendations_response = personalize_runtime.get_recommendations(
        campaignArn = base_campaign_arn,
        userId = user_id,
        numResults = 10
    )
    
    # 추천 결과 정제
    s3 = boto3.client('s3')
    data_bucket = os.environ['data_bucket']
    csv_file = s3.get_object(
        Bucket=data_bucket,
        Key='dataset/training_item.csv'
        )

    items_df = pd.read_csv(csv_file['Body'])

    items_list = []
    for item in get_recommendations_response['itemList']:
        items_list.append(item['itemId'])   
    df = pd.DataFrame(data={'ITEM_ID':items_list})
    items_list = df.merge(items_df)
    items_list_to_store = items_list.to_csv()

    
    # S3 에 추천 결과 저장
    s3 = boto3.client('s3')
    bucket_name = os.environ['bucket_name']
    
    apnortheast2 = dateutil.tz.gettz('Asia/Seoul')
    prefix= "recommended-list/" + datetime.datetime.now(tz=apnortheast2).strftime("%Y-%m-%d-%H") + "/"

    key_name = 'personalize - userId: ' + user_id + '.csv'
    s3.put_object(Bucket=bucket_name, Key=prefix+key_name, Body=items_list_to_store)
    
    return {
        'statusCode': 200,
        'body': items_list.to_json()
    }
