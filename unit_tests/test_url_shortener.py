from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_short_url():
    response = client.post("/url/shorten", json={"url": "https://www.wikipedia.com"})
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_redirect_to_url():
    response = client.post("/url/shorten", json={"url": "https://www.wikipedia.com"})
    short_url = response.json()["short_url"]
    redirect_response = client.get(f"{short_url}", allow_redirects=False)
    assert redirect_response.status_code == 307

def test_metrics():
    urls = [
        "https://www.wikipedia.com",
        "https://www.app.com/page1",
        "https://www.newapp.org",
        "https://www.newapp.org/page1",
        "https://www.oldapp.com/old",
        "https://www.oldapp.com",
    ]
    for url in urls:
        client.post("/url/shorten", json={"url": url})
    response = client.get("/url/metrics")
    assert response.status_code == 200
    assert "www.oldapp.com" in response.json()
    assert response.json()["www.newapp.org"] == 2