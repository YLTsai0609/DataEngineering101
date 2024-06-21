import json
import boto3
import random
import os

def handler(event, context):
    s3 = boto3.client('s3')
    data_bucket = os.environ['data_bucket']
    response = s3.get_object(
        Bucket=data_bucket,
        Key= event['Records'][0]['s3']['object']['key']
        )

    text_data = response['Body'].read().decode('utf-8')
    
    dicts = text_data.split('}')
    dicts = list(filter(None, dicts))
    items_list = [json.loads(d + '}') for d in dicts]
    
    model_list = []
    model_click = {
        'model_AP': 0,
        'model_SM': 0
    }
    for item in items_list:
        model_list.append(item['model'])
        if item['model'] == 'model_AP':
            model_click['model_AP'] += item['clickYn']
        else:
            model_click['model_SM'] += item['clickYn']
    
    model_count_ap = model_list.count('model_AP')
    model_count_sm = model_list.count('model_SM')

    dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')
    table_name = 'Model'
    update_requests = [
        {
            'Update': {
                'TableName': table_name,
                'Key': {'id': {'S': '1'}, 'model_name': {'S': 'model_AP'}},
                'UpdateExpression': 'SET invocation_count = invocation_count + :c, reward_click = reward_click + :r',
                'ExpressionAttributeValues': {':c': {'N': str(model_count_ap)}, ':r': {'N': str(model_click['model_AP'])}}
            }
        },
        {
            'Update': {
                'TableName': table_name,
                'Key': {'id': {'S': '2'}, 'model_name': {'S': 'model_SM'}},
                'UpdateExpression': 'SET invocation_count = invocation_count + :c, reward_click = reward_click + :r',
                'ExpressionAttributeValues': {':c': {'N': str(model_count_sm)}, ':r': {'N': str(model_click['model_SM'])}}
            }
        }
    ]
    dynamodb.transact_write_items(TransactItems=update_requests)

    return {
        'statusCode': 200
    }
