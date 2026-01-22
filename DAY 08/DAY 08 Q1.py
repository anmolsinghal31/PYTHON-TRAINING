import requests
import json


def fetch_and_save_data():
    # 1. URL for a public REST API (using restful-api.dev based on your image)
    url = "https://api.restful-api.dev/objects"

    # 2. Sending custom headers with the request
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "PythonAutomationScript/1.0"
    }

    try:
        # 1. Send GET request
        response = requests.get(url, headers=headers)

        # 5. Handle HTTP errors using proper exception handling
        response.raise_for_status()

        # 3. Parse JSON response
        all_objects = response.json()

        # 3. Extract specific fields (e.g., just Name and ID)
        extracted_data = []
        for obj in all_objects[:5]:  # Taking first 5 items for the example
            info = {
                "id": obj.get("id"),
                "name": obj.get("name")
            }
            extracted_data = info

        # 4. Serialize the extracted data and save it into a JSON file
        with open("extracted_objects.json", "w") as json_file:
            json.dump(extracted_data, json_file, indent=4)

        print("Success! Data has been saved to 'extracted_objects.json'.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    fetch_and_save_data()