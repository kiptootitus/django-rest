import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/?"

get_response = requests.get(endpoint)

print(get_response.json())

#Json -> is Jascript Object Notion 
print(get_response.status_code)