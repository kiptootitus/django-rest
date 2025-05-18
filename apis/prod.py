from getpass import getpass

import requests


auth_endpoint = 'http://localhost:8000/api/auth/'

username = input("Enter your username: ")
password = getpass("Enter your password: ")

auth_response = requests.post(auth_endpoint, json={"username":username, "password":password})
print(auth_response.json())

if auth_response.status_code ==200:
    Bearer = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {Bearer}"
    }
    endpoint = 'http://127.0.0.1:8000/api/products/create/'
    data = {"name": "testing 1 2 3", "description": "Using api calls prod", "price": 500.97, "weight": 1.3}
    endpoint_response = requests.post(endpoint, headers=headers, json=data)

    print(endpoint_response.json())
    print(endpoint_response.status_code)


else:
    print("Product cannot be created at this time")