import requests

endpoint = "http://localhost:8000/"

# res = requests.get(endpoint)
res = requests.get(endpoint,json={"query": "Hello World"})
print(res.text)