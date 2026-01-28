import pytest

# The function to test
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Requirement 3: Use assert statements to validate results
def test_divide_success():
    """Test standard division with valid inputs."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_float():
    """Test division resulting in a float."""
    assert divide(5, 2) == 2.5

# Requirement 4: Validate that an exception is raised for division by zero
def test_divide_by_zero():
    """Verify that ZeroDivisionError is raised when b is 0."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10, 0)

    # Asserting the error message matches
    assert str(excinfo.value) == "Cannot divide by zero"