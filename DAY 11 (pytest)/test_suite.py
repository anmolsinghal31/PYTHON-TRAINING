import pytest
import sys
# Import the functions we want to verify from our logic file
from app_logic import multiply, divide, login 

#ASSERTIONS & ERROR HANDLING

def test_addition():
    # Basic sanity check
    assert 2 + 3 == 5

def test_subtraction():
    # Intentionally failing this to show a custom error message
    # In real tests, we use these messages to debug faster
    assert 5 - 3 == 1, "Expected 2, but the calculation failed"

def test_divide_by_zero():
    # We use pytest.raises when we EXPECT an error to happen
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


#UNIT & FUNCTIONAL TESTS

def test_multiply_logic():
    # Unit test: checks one specific function in isolation
    assert multiply(3, 4) == 12

@pytest.mark.smoke
def test_admin_login_flow():
    # Functional test: checks a user workflow (Admin Login)
    # Marked as 'smoke' so we can run it quickly after a deployment
    result = login("admin", "admin123")
    assert result == "Login Successful"


#TEST CONTROL (SKIPS & XFAILS)

@pytest.mark.skip(reason="Work in progress - ticket #405")
def test_payment_gateway():
    # Skip this because the API isn't built yet
    assert True

@pytest.mark.skipif(sys.platform == "win32", reason="Feature only works on Linux/Mac")
def test_os_specific_feature():
    # Prevents tests from breaking when run on the wrong OS
    assert True

@pytest.mark.xfail(reason="Known bug in the multiplier for negative numbers")
def test_negative_multiply():
    # We know this fails, but we don't want it to stop our CI pipeline
    assert multiply(-1, -1) == -5