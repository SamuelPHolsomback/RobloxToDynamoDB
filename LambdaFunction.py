import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Test')

def convert_decimal(d):
    if isinstance(d, Decimal):
        return float(d)
    return d

def convert_item(item):
    if isinstance(item, dict):
        return {k: convert_item(v) for k, v in item.items()}
    elif isinstance(item, list):
        return [convert_item(x) for x in item]
    else:
        return convert_decimal(item)

def lambda_handler(event, context):
    body = event.get('body', '{}')  # Default to '{}' if 'body' key is missing

    try:
        parsed_body = json.loads(body)
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid JSON in request body')
        }

    action = parsed_body.get('action', '').upper()

    if action == "WRITE":
        items = parsed_body.get('items')
        if not items:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing items key in the request body')
            }
        
        for item in items:
            table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Items written successfully')
        }

    elif action == "READ":
        primaryKey = parsed_body.get('ID')
        if not primaryKey:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing ID key in the request body for READ action')
            }
        
        key = {'ID': primaryKey}
        response = table.get_item(Key=key)
        item = response.get('Item')

        if item:
            item = convert_item(item)
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'ID': primaryKey, 'message': 'Item not found'})
            }

    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unknown action, please pass WRITE or READ for action.')
        }
