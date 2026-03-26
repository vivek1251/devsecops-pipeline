import pytest
import sqlite3
import os
from unittest.mock import patch

os.environ['FLASK_SECRET'] = 'test-secret-key'

from app import app, get_db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # NOSONAR
    with app.test_client() as client:
        yield client


# ── Health endpoint ──────────────────────────────────────────────────────────

def test_health_returns_200(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_health_returns_healthy_status(client):
    response = client.get('/health')
    assert response.get_json() == {"status": "healthy"}

def test_health_post_not_allowed(client):
    response = client.post('/health')
    assert response.status_code == 405

def test_health_delete_not_allowed(client):
    response = client.delete('/health')
    assert response.status_code == 405

def test_health_put_not_allowed(client):
    response = client.put('/health')
    assert response.status_code == 405


# ── Search endpoint ──────────────────────────────────────────────────────────

def test_search_returns_200(client):
    response = client.get('/search?name=alice')
    assert response.status_code == 200

def test_search_returns_result_key(client):
    response = client.get('/search?name=alice')
    assert 'result' in response.get_json()

def test_search_empty_name(client):
    response = client.get('/search?name=')
    assert response.status_code == 200

def test_search_no_param(client):
    response = client.get('/search')
    assert response.status_code == 200

def test_search_result_is_string(client):
    response = client.get('/search?name=test')
    data = response.get_json()
    assert isinstance(data['result'], str)

def test_search_special_characters(client):
    response = client.get('/search?name=test%20user')
    assert response.status_code == 200

def test_search_post_not_allowed(client):
    response = client.post('/search')
    assert response.status_code == 405

def test_search_long_name(client):
    response = client.get('/search?name=' + 'a' * 200)
    assert response.status_code == 200

def test_search_numeric_name(client):
    response = client.get('/search?name=12345')
    assert response.status_code == 200

def test_search_returns_list_in_result(client):
    response = client.get('/search?name=nobody')
    data = response.get_json()
    assert '[]' in data['result']


# ── User endpoint ────────────────────────────────────────────────────────────

def test_user_returns_200(client):
    with patch('app.os.system') as mock_sys:
        mock_sys.return_value = 0
        response = client.get('/user?username=alice')
    assert response.status_code == 200

def test_user_returns_username_in_response(client):
    with patch('app.os.system') as mock_sys:
        mock_sys.return_value = 0
        response = client.get('/user?username=alice')
    assert response.get_json()['user'] == 'alice'

def test_user_no_param(client):
    with patch('app.os.system') as mock_sys:
        mock_sys.return_value = 0
        response = client.get('/user')
    assert response.status_code == 200

def test_user_empty_username(client):
    with patch('app.os.system') as mock_sys:
        mock_sys.return_value = 0
        response = client.get('/user?username=')
    assert response.get_json()['user'] == ''

def test_user_calls_os_system(client):
    with patch('app.os.system') as mock_sys:
        mock_sys.return_value = 0
        client.get('/user?username=testuser')
        mock_sys.assert_called_once_with('echo testuser')

def test_user_post_not_allowed(client):
    response = client.post('/user')
    assert response.status_code == 405

def test_user_special_chars(client):
    with patch('app.os.system') as mock_sys:
        mock_sys.return_value = 0
        response = client.get('/user?username=test-user_123')
    assert response.status_code == 200

def test_user_long_username(client):
    with patch('app.os.system') as mock_sys:
        mock_sys.return_value = 0
        response = client.get('/user?username=' + 'b' * 100)
    assert response.status_code == 200


# ── get_db helper ────────────────────────────────────────────────────────────

def test_get_db_returns_connection():
    conn = get_db()
    assert conn is not None
    conn.close()

def test_get_db_creates_users_table():
    conn = get_db()
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    ).fetchall()
    assert len(tables) == 1
    conn.close()

def test_get_db_table_has_id_column():
    conn = get_db()
    cursor = conn.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in cursor.fetchall()]
    assert 'id' in columns
    conn.close()

def test_get_db_table_has_name_column():
    conn = get_db()
    cursor = conn.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in cursor.fetchall()]
    assert 'name' in columns
    conn.close()

def test_get_db_table_has_password_column():
    conn = get_db()
    cursor = conn.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in cursor.fetchall()]
    assert 'password' in columns
    conn.close()

def test_get_db_idempotent():
    conn1 = get_db()
    conn1.close()
    conn2 = get_db()
    conn2.close()


# ── General app behaviour ────────────────────────────────────────────────────

def test_404_on_unknown_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_app_is_not_none():
    assert app is not None

def test_app_testing_mode(client):
    assert app.config['TESTING'] is True