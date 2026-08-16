from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_contact_form():

    response = client.post(
        "/contact",
        json={
            "name": "Emely",
            "email": "test@example.com",
            "message": "Testing my contact form"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Your message has been sent successfully."


def test_contact_form_allows_browser_origin():
    headers = {
        "Origin": "http://localhost:5500",
        "Access-Control-Request-Method": "POST",
    }

    response = client.options(
        "/contact",
        headers=headers,
    )

    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "*"
    assert "POST" in response.headers.get("access-control-allow-methods", "")