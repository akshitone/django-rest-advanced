import requests

endpoint = "http://localhost:8000/api/products/"

product = {
    "title": "Title 04",
    # "content": "This is a product 04",
    "price": 12.85
}
post_response = requests.post(endpoint, json=product)
print(post_response.json())
