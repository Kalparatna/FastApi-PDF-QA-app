import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_websocket_qa():
    with client.websocket_connect("/ws/qa/") as websocket:
        websocket.send_text("What is the content of the uploaded PDF?")
        response = websocket.receive_text()
        assert "content" in response
