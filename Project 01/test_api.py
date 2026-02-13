import requests

def test_restaurant_reg():
    url = "http://127.0.0.1:5000/api/v1/restaurants"
    payload = {"name": "Test Cafe", "location": "Noida"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201