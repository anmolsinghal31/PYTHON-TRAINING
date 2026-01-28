import pytest

@pytest.fixture
def data():
    return [1, 2, 3]

# Add 'data' as a parameter here
def test_one(data):
    assert 2 in data
    print(data)

# Add 'data' as a parameter here
def test_two(data):
    assert len(data) == 3
    print(len(data))