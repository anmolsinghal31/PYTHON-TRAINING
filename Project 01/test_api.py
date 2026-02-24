import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_restaurant(client):
    response = client.post('/api/v1/restaurants', json={'name': 'Test Rest'})
    assert response.status_code == 201

def test_add_dish(client):
    response = client.post('/api/v1/dishes', json={'dish_name': 'Pizza'})
    assert response.status_code == 201

def test_register_user(client):
    response = client.post('/api/v1/users', json={'username': 'anmol'})
    assert response.status_code == 201

def test_place_order(client):
    response = client.post('/api/v1/orders', json={'item': 'Pizza'})
    assert response.status_code == 201

def test_admin_approve(client):
    response = client.post('/api/v1/admin/approve', json={'id': 1})
    assert response.status_code == 200

# pytest test_api.py --html=pytest_report_$(date +%Y%m%d_%H%M%S).html --self-contained-html