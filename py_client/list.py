import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input("What is you username?\n")
password = getpass("Enter your password\n")

auth_response = requests.post(auth_endpoint, json = {'username' : username, 'password' : password})
print(auth_response.json())

if auth_response.status_code == 200:
    print("status code is 200")
    token = auth_response.json()['token']
    print(f"token is {token}")
    headers = {
        "Authorization": f"Bearer {token}"
    }

    print(headers)
    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint, headers = headers)
    print(get_response.json())