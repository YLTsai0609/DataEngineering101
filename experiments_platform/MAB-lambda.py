import json
import boto3
import random

def handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')
    params = {
        'TableName': 'Model',
    }
    
    model_list = dynamodb.scan(**params)
    
    # 모델 선정
    probs = []
    for v in model_list['Items']:
        success = int(v["reward_click"]['N'])
        failure = int(v["invocation_count"]['N']) - success
        probs.append(random.betavariate(1 + success, 1 + failure))

    model_index = max(range(len(probs)), key=lambda x: probs[x])
    model_name =  model_list['Items'][model_index]["model_name"].get('S')

    total_invocation = 0
    total_invocation = sum([int(model.get('invocation_count', {}).get('N', 0)) for model in model_list['Items']])

    payload = {
        'userId': random.randrange(1,100), # use mab method here instead of random picking
        'totalInvocation': total_invocation
    }
    
    # 모델 invoke
    lambda_client = boto3.client('lambda')
    if model_name == 'model_AP': 
        # invoke Personalize Model
        response = lambda_client.invoke(
            FunctionName='PersonalizeListFunction',
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        result = json.loads(response['Payload'].read())
    else:
        # invoke SageMaker Model
        response = lambda_client.invoke(
            FunctionName='SageMakerListFunction',
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        result = json.loads(response['Payload'].read())
    
    # 요청 & 클릭 데이터 생성
    payload['model'] = model_name
    lambda_client.invoke(
        FunctionName='SimulateStreamFunction',
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )

    return {
        'statusCode': 200,
        'body': result['body']
    }
