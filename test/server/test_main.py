from fastapi.testclient import TestClient
from server.main import app


def test_hello():
    assert "hello" == "hello"


client = TestClient(app)


def test_sample_endpoint():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
