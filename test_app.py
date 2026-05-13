import app

def test_home():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"

def test_health():
    client = app.app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert "uptime_seconds" in data
    assert data["status"] in ["healthy", "unhealthy"]

def test_metrics():
    client = app.app.test_client()
    response = client.get('/metrics')
    assert response.status_code == 200
    assert "app_cpu_percent" in response.data.decode()
