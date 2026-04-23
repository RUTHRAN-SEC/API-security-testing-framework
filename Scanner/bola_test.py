import requests

BASE_URL = "http://127.0.0.1:5000"

for user_id in range(1, 5):
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    print(f"User {user_id}: {response.json()}")
