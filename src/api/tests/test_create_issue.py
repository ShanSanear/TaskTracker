from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from ..main import api

client = TestClient(api)


@pytest.fixture(autouse=True)
def create_user(local_sqlite_dbn):
    new_account_name = "TestUser"
    new_account_email = "TestEmail@domain.com"
    response = client.post(
        "/users/", json={"name": new_account_name, "email": new_account_email}
    )
    response.raise_for_status()


def test_create_new_issue():
    issue_summary = "Test issue summary"
    response = client.post(
        "/issue/", json={"summary": issue_summary}
    )
    assert response.status_code == HTTPStatus.CREATED
    response_content = response.json()
    assert response_content["issue_id"] == 1
    assert response_content["summary"] == issue_summary
    assert response_content["description"] is None


