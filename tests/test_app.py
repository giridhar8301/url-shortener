import pytest
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_shorten_valid_url(client):
    res = client.post("/api/shorten", json={"url": "https://example.com"})
    assert res.status_code == 201
    assert "short_code" in res.json

def test_shorten_invalid_url(client):
    res = client.post("/api/shorten", json={"url": "invalid"})
    assert res.status_code == 400

def test_redirect(client):
    res = client.post("/api/shorten", json={"url": "https://example.com"})
    code = res.json["short_code"]

    r = client.get(f"/{code}", follow_redirects=False)
    assert r.status_code == 302

def test_redirect_invalid(client):
    r = client.get("/bad123")
    assert r.status_code == 404

def test_stats(client):
    res = client.post("/api/shorten", json={"url": "https://example.com"})
    code = res.json["short_code"]
    client.get(f"/{code}")

    stats = client.get(f"/api/stats/{code}")
    assert stats.status_code == 200
    assert "clicks" in stats.json
