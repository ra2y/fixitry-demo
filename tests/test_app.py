from app.main import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_config_status_does_not_expose_secret():
    client = app.test_client()
    response = client.get("/api/config-status")
    payload = response.get_json()

    assert response.status_code == 200
    assert set(payload) == {"payment_api_key_configured"}
    assert "demo-super-secret-key-12345" not in response.get_data(as_text=True)

