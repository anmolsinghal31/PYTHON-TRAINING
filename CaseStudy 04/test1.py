import pytest
import requests
from unittest.mock import patch
from bs4 import BeautifulSoup


# API Automation with Mocking
@patch('requests.get')
def test_api_fetch_patients(mock_get):
    # Simulating what the API would return
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"name": "Aman", "age": 22, "disease": "Fever"}
    ]

    response = requests.get("http://fake-hospital.com/api/patients")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Aman"


# Web Scraping Task (using a string instead of a live URL)
def test_web_scraping_logic():
    fake_html = "<html><table><tr><td>Aman</td><td>22</td><td>Fever</td></tr></table></html>"
    soup = BeautifulSoup(fake_html, 'html.parser')
    name = soup.find('td').text
    assert name == "Aman"


@pytest.mark.parametrize("name", ["Patient_A", "Patient_B"])
def test_parameterized_patients(name):
    assert len(name) > 0