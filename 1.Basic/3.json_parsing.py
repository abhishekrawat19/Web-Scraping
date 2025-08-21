# json_parsing.py

import requests
import json

# A public API that provides placeholder JSON data
URL = "https://jsonplaceholder.typicode.com/todos/1"

def fetch_and_parse_json():
    """
    Fetches data from a JSON API and parses it.
    """
    print(f"--- Fetching data from JSON API: {URL} ---")
    try:
        # Make a GET request to the API endpoint
        response = requests.get(URL)
        response.raise_for_status() # Check for any request errors

        # Use the .json() method from the requests library to parse the response
        # This is the most convenient way.
        data = response.json()

        print("Successfully parsed JSON data using response.json():")
        print(f"User ID: {data['userId']}")
        print(f"Title: {data['title']}")
        print(f"Completed: {data['completed']}")

        # Alternatively, you can parse the text content using the json library
        # This is useful if you get JSON from a source other than a web request.
        # data_manual = json.loads(response.text)
        # print("\nManually parsed with json.loads():", data_manual)
        
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch the URL: {e}")
    except json.JSONDecodeError:
        print("Failed to decode JSON from the response.")
    except KeyError as e:
        print(f"A key was not found in the JSON response: {e}")

if __name__ == "__main__":
    fetch_and_parse_json()