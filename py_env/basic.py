import requests


endpoint = "https://httpbin/org/status/200/"
endpoint = "http://127.0.0.1:8000/api/"
# sending data to api page i.e api_home view 

get_response = requests.post(endpoint,json = {"title": "Hello world"})

print(get_response.json())
