# requests_example.py

import requests

# A simple website for testing HTTP requests
BASE_URL = "http://httpbin.org"

def make_get_request():
    """
    Makes a GET request to fetch data.
    GET is used to request data from a specified resource.
    """
    print("--- Making a GET request ---")
    try:
        # Append '/get' to the base URL
        response = requests.get(f"{BASE_URL}/get", params={'key1': 'value1', 'key2': 'value2'})
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        
        # The response from httpbin.org/get is JSON, so we can use .json()
        data = response.json()
        print("Response JSON:")
        print(data)
        print(f"Your IP address is: {data['origin']}")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def make_post_request():
    """
    Makes a POST request to submit data.
    POST is used to send data to a server to create/update a resource.
    """
    print("\n--- Making a POST request ---")
    try:
        # Define the payload (data to be sent)
        payload = {'username': 'testuser', 'password': 'password123'}
        
        # Append '/post' to the base URL and send the payload
        response = requests.post(f"{BASE_URL}/post", data=payload)
        
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        
        # The response from httpbin.org/post will include the form data we sent
        data = response.json()
        print("Response JSON:")
        print(data)
        print(f"Data sent: {data['form']}")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    make_get_request()
    make_post_request()