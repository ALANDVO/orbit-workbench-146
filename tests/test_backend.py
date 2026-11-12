from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_summarize():
    response = client.post("/summarize", json={"text": "Hello world"})
    assert response.status_code == 200
    assert response.json() == {"word_count": 2}
