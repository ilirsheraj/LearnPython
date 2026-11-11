import requests
import json

url = "https://httpbin.org/post"
data = dict(title = "Learn Python Programming")

resp = requests.post(url, data)
print("Response for POST")
# print(resp.json())
print(json.dumps(resp.json(), indent=4))