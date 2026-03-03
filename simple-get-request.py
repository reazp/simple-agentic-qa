import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    
    data = response.json()
    print(data)
    assert data["userId"] == 1
    assert "title" in data
    assert data["id"] == 1