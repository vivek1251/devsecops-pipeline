import pytest
import os
os.environ['APP_SECRET_KEY'] = 'test-secret-key'

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'

def test_search_empty(client):
    response = client.get('/search?name=')
    assert response.status_code == 200

def test_search_with_name(client):
    response = client.get('/search?name=alice')
    assert response.status_code == 200
    assert 'result' in response.get_json()

def test_user_endpoint(client):
    response = client.get('/user?username=vivek')
    assert response.status_code == 200
    assert response.get_json()['user'] == 'vivek'

def test_user_empty(client):
    response = client.get('/user?username=')
    assert response.status_code == 200