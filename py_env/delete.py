import requests



# takes the detail of product one
# sending data to api page i.e api_home view 
product_id = input('Enter the product id to delete\n')
try:
    product_id = int(product_id)
except:
    product_id  = None
    print(f'product id is not valid')

if product_id is not None:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)

