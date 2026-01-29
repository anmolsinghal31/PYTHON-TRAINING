import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user_and_create_post():
    # 1. Fetch a user
    user_res = requests.get(f"{BASE_URL}/users/1")
    assert user_res.status_code == 200
    user_id = user_res.json()['id']

    # 2. Create a post for that user (E2E flow)
    payload = {"title": "Pytest E2E", "body": "Testing parallel execution", "userId": user_id}
    post_res = requests.post(f"{BASE_URL}/posts", json=payload)

    assert post_res.status_code == 201
    assert post_res.json()['title'] == "Pytest E2E"


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_multiple_posts(post_id):
    # This helps demonstrate parallel execution later
    res = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert res.status_code == 200