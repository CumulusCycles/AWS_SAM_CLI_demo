import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('demo-app-tbl')

def lambda_handler(event, context):
    response = table.get_item(
        Key = {
            'ID':'1'
        }
    )
    
    visit_count = response['Item']['counter'] 
    visit_count = str(int(visit_count) + 1)
    
    response = table.put_item(
        Item = {
            'ID':'1',
            'counter': visit_count
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': visit_count
    }