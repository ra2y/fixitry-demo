from app.main import app


def test_find_user_returns_match():
    response = app.test_client().get("/api/users?name=alice")

    assert response.status_code == 200
    assert response.get_json() == [{"id": 1, "name": "alice", "role": "admin"}]


def test_find_user_unknown_returns_empty_list():
    response = app.test_client().get("/api/users?name=nobody")

    assert response.status_code == 200
    assert response.get_json() == []


def test_read_note_returns_content():
    response = app.test_client().get("/api/notes?file=welcome.txt")

    assert response.status_code == 200
    assert response.get_json() == {"content": "Welcome to the SecureFix demo."}


def test_greet_includes_name():
    response = app.test_client().get("/api/greet?name=Ana")

    assert response.status_code == 200
    assert "Hello Ana" in response.get_data(as_text=True)


def test_checksum_is_stable_hex():
    client = app.test_client()
    first = client.get("/api/checksum?text=hello").get_json()["checksum"]
    second = client.get("/api/checksum?text=hello").get_json()["checksum"]

    assert first == second
    assert first and all(c in "0123456789abcdef" for c in first)