import pytest
import json
from app2 import app, create_resources, dynamodb, s3, TABLE_NAME, BUCKET_NAME

# Initialize the Flask test client and create resources
@pytest.fixture(scope='module')
def client():
    create_resources()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def get_s3_object(bucket, key):
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read().decode('utf-8')
    except s3.exceptions.NoSuchKey:
        return None

def test_get_item(client):
    item_id = 'get-item-id'
    item_data = {'name': 'Get Item', 'value': 'This item should be retrieved.'}
    client.post(f'/items/{item_id}', data=json.dumps(item_data), content_type='application/json')
    
    response = client.get(f'/items/{item_id}')
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['id'] == item_id
    assert response_json['name'] == 'Get Item'
    assert response_json['value'] == 'This item should be retrieved.'
    assert json.loads(get_s3_object(BUCKET_NAME, item_id)) == json.dumps(item_data)

def test_get_item_not_found(client):
    response = client.get('/items/nonexistent-item-id')
    assert response.status_code == 404
    response_json = json.loads(response.data)
    assert response_json['error'] == 'Item not found'

def test_get_item_no_params(client):
    response = client.get('/items/')
    assert response.status_code == 404
    response_json = json.loads(response.data)
    assert response_json['error'] == 'Invalid request'

def test_get_item_incorrect_params(client):
    response = client.get('/items/invalid-id?param=extra')
    assert response.status_code == 404
    response_json = json.loads(response.data)
    assert response_json['error'] == 'Invalid request'

def test_post_create_item(client):
    item_id = 'post-create-item-id'
    item_data = {'name': 'Post Create Item', 'value': 'This item should be created.'}
    
    response = client.post(f'/items/{item_id}', data=json.dumps(item_data), content_type='application/json')
    assert response.status_code == 201
    response_json = json.loads(response.data)
    assert response_json['id'] == item_id
    assert response_json['name'] == 'Post Create Item'
    assert response_json['value'] == 'This item should be created.'
    assert json.loads(get_s3_object(BUCKET_NAME, item_id)) == json.dumps(item_data)

def test_post_duplicate_item(client):
    item_id = 'post-duplicate-item-id'
    item_data = {'name': 'Post Duplicate Item', 'value': 'This item should be duplicated.'}
    
    client.post(f'/items/{item_id}', data=json.dumps(item_data), content_type='application/json')
    response = client.post(f'/items/{item_id}', data=json.dumps(item_data), content_type='application/json')
    
    assert response.status_code == 400
    response_json = json.loads(response.data)
    assert response_json['error'] == 'Item already exists'

def test_put_update_item(client):
    item_id = 'put-update-item-id'
    initial_data = {'name': 'Initial Item', 'value': 'Initial value.'}
    updated_data = {'name': 'Updated Item', 'value': 'Updated value.'}
    
    client.post(f'/items/{item_id}', data=json.dumps(initial_data), content_type='application/json')
    response = client.put(f'/items/{item_id}', data=json.dumps(updated_data), content_type='application/json')
    
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['id'] == item_id
    assert response_json['name'] == 'Updated Item'
    assert response_json['value'] == 'Updated value.'
    assert json.loads(get_s3_object(BUCKET_NAME, item_id)) == json.dumps(updated_data)

def test_put_item_not_found(client):
    item_id = 'put-item-not-found-id'
    updated_data = {'name': 'Updated Item', 'value': 'Updated value.'}
    
    response = client.put(f'/items/{item_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 404
    response_json = json.loads(response.data)
    assert response_json['error'] == 'Item not found'

def test_delete_item(client):
    item_id = 'delete-item-id'
    item_data = {'name': 'Delete Item', 'value': 'This item should be deleted.'}
    
    client.post(f'/items/{item_id}', data=json.dumps(item_data), content_type='application/json')
    response = client.delete(f'/items/{item_id}')
    
    assert response.status_code == 204
    assert get_s3_object(BUCKET_NAME, item_id) is None
    
    response = client.get(f'/items/{item_id}')
    assert response.status_code == 404
    response_json = json.loads(response.data)
    assert response_json['error'] == 'Item not found'

def test_delete_item_not_found(client):
    item_id = 'delete-item-not-found-id'
    
    response = client.delete(f'/items/{item_id}')
    assert response.status_code == 404
    response_json = json.loads(response.data)
    assert response_json['error'] == 'Item not found'

if __name__ == '__main__':
    pytest.main()
