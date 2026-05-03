"""Functional test: HTTP API payment servisa kao celine."""
from fastapi.testclient import TestClient


def test_get_nonexistent_order_returns_404():
    from main import app

    client = TestClient(app)
    resp = client.get("/orders/does-not-exist")

    assert resp.status_code == 404
    assert resp.json()["detail"] == "Order not found"
