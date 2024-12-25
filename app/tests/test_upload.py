import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_pdf():
    with open("test.pdf", "rb") as pdf:
        response = client.post("/api/upload/", files={"file": pdf})
        assert response.status_code == 200
        assert "text extracted successfully" in response.json()["message"]
