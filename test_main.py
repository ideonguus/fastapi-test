from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_item():
    response = client.get("/users/123")
    assert response.status_code == 200
    assert response.json() == {"user_id": 123}
