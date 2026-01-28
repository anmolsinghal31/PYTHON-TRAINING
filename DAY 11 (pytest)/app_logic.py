# --- MATH OPERATIONS ---

def multiply(a, b):
    """Simple multiplier for unit testing."""
    return a * b

def divide(a, b):
    """Returns quotient; used to demonstrate exception handling."""
    return a / b


# --- AUTHENTICATION LOGIC ---

def login(username, password):
    """
    Simulates a login check.
    In a real app, this would check a database.
    """
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Credentials"