from .conftest import client


def test_get_login(client):
    response = client.get("/login")

    assert response.status_code == 200


def test_post_login(client):
    email = "test@mail.com"
    password = "P@$$w0rd123"

    data = {"email": email, "password": password}

    with client.application.app_context():
        response = client.post("/login", data=data)

    assert response.status_code == 200


def test_get_register(client):
    pass


def test_post_register(client):
    pass
