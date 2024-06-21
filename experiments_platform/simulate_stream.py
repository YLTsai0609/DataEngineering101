
import json
import boto3
import random
import datetime

kinesis = boto3.client('firehose')

def handler(event, context):
    event['clickYn'] = 0
    if int(event['totalInvocation']) > 200:
        if event['model'] == 'model_AP':
            event['clickYn'] = 1 if random.randint(0,50) in [0,1,2] else 0
    else:
        event['clickYn'] = 1 if random.randint(0,99) in [0,1,2] else 0
    kinesis.put_record(
        DeliveryStreamName='PUT-S3-dynamic',
        Record={
            'Data': json.dumps(event)
        }
    )
    return {
        'statusCode': 200
    }
