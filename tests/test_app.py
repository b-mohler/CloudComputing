import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_item(client):
    response = client.post('/items/1', json={'name': 'item1'})
    assert response.status_code == 201
    assert response.json == {'name': 'item1'}

def test_get_item(client):
    client.post('/items/2', json={'name': 'item2'})
    response = client.get('/items/2')
    assert response.status_code == 200
    assert response.json == {'name': 'item2'}

def test_update_item(client):
    client.post('/items/3', json={'name': 'item3'})
    response = client.put('/items/3', json={'name': 'item3-updated'})
    assert response.status_code == 200
    assert response.json == {'name': 'item3-updated'}

def test_delete_item(client):
    client.post('/items/4', json={'name': 'item4'})
    response = client.delete('/items/4')
    assert response.status_code == 204
    response = client.get('/items/4')
    assert response.status_code == 404
