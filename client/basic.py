import requests

endpoint = "http://localhost:8000/api/"

post_response = requests.post(endpoint, json={
                              "title": "Title 03", "price": 15.75, "content": "This is content 03"})
print(post_response.text)
