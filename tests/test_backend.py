from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_summarize():
    response = client.post("/summarize", json={"text": "Hello world"})
    assert response.status_code == 200
    assert response.json() == {"word_count": 2}

def test_summarize_strict_valid():
    response = client.post("/summarize/strict", json={"text": "Hello world"})
    assert response.status_code == 200
    assert response.json() == {"word_count": 2}

def test_summarize_strict_empty():
    response = client.post("/summarize/strict", json={"text": ""})
    assert response.status_code == 422

def test_summarize_strict_whitespace():
    response = client.post("/summarize/strict", json={"text": "   \n  "})
    assert response.status_code == 422
