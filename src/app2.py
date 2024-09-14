# app.py

from flask import Flask, request, jsonify
import boto3
from botocore.exceptions import ClientError
import uuid

app = Flask(__name__)

# Initialize AWS clients with LocalStack
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localstack:4566')
s3 = boto3.client('s3', endpoint_url='http://localstack:4566')

# DynamoDB table and S3 bucket names
TABLE_NAME = 'items'
BUCKET_NAME = 'mybucket'

# Create table and bucket if they do not exist
def create_resources():
    try:
        dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] != 'ResourceInUseException':
            raise

    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
    except ClientError as e:
        if e.response['Error']['Code'] != 'BucketAlreadyOwnedByYou':
            raise

create_resources()

table = dynamodb.Table(TABLE_NAME)

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    try:
        response = table.get_item(Key={'id': item_id})
        item = response.get('Item')
        if item:
            s3_object = s3.get_object(Bucket=BUCKET_NAME, Key=item_id)
            item['s3_object'] = s3_object['Body'].read().decode('utf-8')
            return jsonify(item), 200
        return jsonify({'error': 'Item not found'}), 404
    except ClientError:
        return jsonify({'error': 'Error accessing S3'}), 500

@app.route('/items/<item_id>', methods=['POST'])
def create_item(item_id):
    if table.get_item(Key={'id': item_id}).get('Item'):
        return jsonify({'error': 'Item already exists'}), 400

    item = request.json
    item['id'] = item_id

    try:
        table.put_item(Item=item)
        s3.put_object(Bucket=BUCKET_NAME, Key=item_id, Body=str(item))
        return jsonify(item), 201
    except ClientError:
        return jsonify({'error': 'Error accessing S3'}), 500

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if not table.get_item(Key={'id': item_id}).get('Item'):
        return jsonify({'error': 'Item not found'}), 404

    item = request.json
    item['id'] = item_id

    try:
        table.put_item(Item=item)
        s3.put_object(Bucket=BUCKET_NAME, Key=item_id, Body=str(item))
        return jsonify(item), 200
    except ClientError:
        return jsonify({'error': 'Error accessing S3'}), 500

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if not table.get_item(Key={'id': item_id}).get('Item'):
        return jsonify({'error': 'Item not found'}), 404

    try:
        table.delete_item(Key={'id': item_id})
        s3.delete_object(Bucket=BUCKET_NAME, Key=item_id)
        return '', 204
    except ClientError:
        return jsonify({'error': 'Error accessing S3'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
