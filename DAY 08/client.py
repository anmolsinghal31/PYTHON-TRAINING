import requests
import time

# The URL of your local Flask server
url = "http://127.0.0.1:5000/users"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Client"
}

def run_test():
    try:
        # 1. PERFORM GET REQUEST
        print("--- Testing GET Request ---")
        response = requests.get(url, headers=headers, timeout=10)
        print("Status Code:", response.status_code)
        print("Data Received:", response.json())
        print("-" * 30)

        # 2. PERFORM POST REQUEST
        print("\n--- Testing POST Request ---")
        body1 = {"name": "Leena"}
        r1 = requests.post(url, json=body1, timeout=10)
        print("Status Code:", r1.status_code)
        print("Data Created:", r1.json())
        print("-" * 30)

        # 3. GET AGAIN TO SEE THE UPDATE
        print("\n--- Verifying Update ---")
        final_check = requests.get(url)
        print("Final User List:", final_check.json())

    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to the server. Make sure 'app.py' is running first!")

if __name__ == "__main__":
    run_test()