import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'
username = input("Please input your username: ")
password = getpass("Please enter your password: ")

# Step 1: Get Auth Token
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})

if auth_response.status_code == 200:
    Bearer = auth_response.json()['token']
    print(f"Token received: {Bearer}")

    headers = {
        "Authorization": f"Bearer {Bearer}"
    }

    # Step 2: Make a GET or POST request to books endpoint
    endpoint = "http://127.0.0.1:8000/api/products/lists/"

    # If you're just trying to get books:
    response = requests.get(endpoint, headers=headers)

    # If you're trying to create a book (you’d need to uncomment this and provide data):
    # data = {"title": "New Book", "author": "You", "description": "Awesome read"}
    # response = requests.post(endpoint, headers=headers, json=data)

    print("Response status:", response.status_code)
    print("Response data:", response.json())

else:
    print("Authentication failed.")
    print(auth_response.status_code)
    print(auth_response.text)
