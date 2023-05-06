import requests


endpoint = "http://127.0.0.1:8000/api/products/1/update/"
# sending data to api page i.e api_home view 

data = {
    'title'  : "new title",
    'price' : 23.22
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())

