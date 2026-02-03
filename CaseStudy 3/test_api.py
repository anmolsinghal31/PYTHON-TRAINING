import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api"


@pytest.fixture
def sample_movie():
    return {
        "movie_name": "The Dark Knight",
        "language": "English",
        "duration": "2h 32m",
        "price": 300
    }


def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_and_get_movie(sample_movie):
    # Post new movie
    post_res = requests.post(f"{BASE_URL}/movies", json=sample_movie)
    assert post_res.status_code == 201
    new_id = post_res.json()['id']

    # Get that specific movie
    get_res = requests.get(f"{BASE_URL}/movies/{new_id}")
    assert get_res.status_code == 200
    assert get_res.json()['movie_name'] == "The Dark Knight"


def test_book_ticket_success():
    payload = {"movie_id": 101, "seats": 2}
    response = requests.post(f"{BASE_URL}/bookings", json=payload)
    assert response.status_code == 201
    assert "booking_id" in response.json()


def test_book_ticket_invalid_movie():
    payload = {"movie_id": 999, "seats": 2}  # 999 doesn't exist
    response = requests.post(f"{BASE_URL}/bookings", json=payload)
    assert response.status_code == 400
    assert response.json()['error'] == "Movie ID not found"


@pytest.mark.parametrize("movie_id", [101, 102])
def test_delete_movies(movie_id):
    response = requests.delete(f"{BASE_URL}/movies/{movie_id}")
    assert response.status_code == 200