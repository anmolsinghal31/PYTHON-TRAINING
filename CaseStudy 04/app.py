import requests
import pytest

# We define the logic for the API calls here
class HospitalAPI:
    def __init__(self):
        self.base_url = "http://fake-hospital-api.com/api"

    def get_patients(self):
        # In a real test, you'd use requests.get()
        # For this assignment, we simulate the JSON response
        return [{"id": 1, "name": "John Doe", "disease": "Flu"}]

    def register_patient(self, data):
        # Simulating a POST request and JSON serialization
        if "name" not in data:
            return {"error": "Missing name"}, 400
        return {"status": "Success", "data": data}, 201

# Pytest using the logic above
def test_get_patients_validation():
    api = HospitalAPI()
    data = api.get_patients()
    assert isinstance(data, list)
    assert data[0]["name"] == "John Doe"

def test_registration_serialization():
    api = HospitalAPI()
    payload = {"name": "Alice", "age": 30, "disease": "Cold"}
    response, status = api.register_patient(payload)
    assert status == 201
    assert response["status"] == "Success"