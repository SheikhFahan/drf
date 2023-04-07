import requests


endpoint = "http://127.0.0.1:8000/api/products/10"
# takes the detail of product one
# sending data to api page i.e api_home view 

get_response = requests.get(endpoint)

print(get_response.json())

