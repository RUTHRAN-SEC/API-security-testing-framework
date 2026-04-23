import requests

url = "http://127.0.0.1:5000/data"

for i in range(100):
    r = requests.get(url)
    print(f"Request {i}: {r.status_code}")
