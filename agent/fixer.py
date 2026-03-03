import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def generate_fix():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()

    return {
        "correct_userId": data["userId"]
    }