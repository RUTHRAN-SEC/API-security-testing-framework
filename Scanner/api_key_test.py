import requests

url = "http://127.0.0.1:5000/config"
r = requests.get(url)

print("Response:", r.json())
