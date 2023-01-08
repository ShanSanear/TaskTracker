from fastapi.testclient import TestClient

from ..app import app

client = TestClient(app)

def test_get_users(local_sqlite_dbn):
    new_account_name = "Name"
    new_account_email = "TestEmail@domain.com"
    response = client.post(
        "/users/", json={"name": new_account_name, "email": new_account_email, "password" : "password1234"}
    )
    assert response.status_code == 200, response.text

    response = client.get("/users/")
    data = response.json()
    assert response.status_code == 200, response.text
    assert new_account_name in data[0]['name']
    assert new_account_email in data[0]['email']
