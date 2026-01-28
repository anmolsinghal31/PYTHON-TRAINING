import pytest

# A fixture with module scope: runs once per test file (module)
@pytest.fixture(scope="module")
def db_connection():
    print("\n[conftest] Connecting to Database (Module Scope)")
    connection = {"status": "connected", "data": [1, 2, 3]}
    yield connection
    print("\n[conftest] Closing Database Connection")

# A fixture with default (function) scope: runs before every single test
@pytest.fixture
def sample_data():
    return {"id": 1, "name": "Test Item"}

import pytest

# --- xUnit-Style Setup/Teardown ---
def setup_module(module):
    print(f"\n[xUnit] setup_module: Preparing {module.__name__}")

def teardown_module(module):
    print(f"\n[xUnit] teardown_module: Cleaning up {module.__name__}")

def setup_function(function):
    print(f"\n[xUnit] setup_function: Setting up {function.__name__}")

def teardown_function(function):
    print(f"\n[xUnit] teardown_function: Tearing down {function.__name__}")


# --- Tests ---
def test_db_read(db_connection):
    print("Running test_db_read...")
    assert db_connection["status"] == "connected"

def test_data_integrity(sample_data):
    print("Running test_data_integrity...")
    assert sample_data["id"] == 1

def test_reusing_db(db_connection):
    """Uses the db_connection from conftest.py"""
    print("Running test_reusing_db in a different file...")
    assert len(db_connection["data"]) == 3

def test_reusing_data(sample_data):
    """Uses the sample_data from conftest.py"""
    print("Running test_reusing_data...")
    assert "name" in sample_data