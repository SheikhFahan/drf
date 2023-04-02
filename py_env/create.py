import requests


endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title'  : "solves the problem",
    'price' : 23.22
}

get_response = requests.post(endpoint, data)
# create a new instance 

print(get_response.json())

