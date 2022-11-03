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


def test_create_new_issue(local_sqlite_dbn):
    issue_summary = "Test issue summary"
    response = client.post(
        "/issues/", json={"summary": issue_summary}
    )
    assert response.status_code == HTTPStatus.CREATED
    response_content = response.json()
    assert response_content["issue_id"] == 1
    assert response_content["summary"] == issue_summary
    assert response_content["description"] is None


def test_change_issue_summary(local_sqlite_dbn):
    issue_summary_initial = "Test issue summary"
    response = client.post(
        "/issues/", json={"summary" : issue_summary_initial}
    )
    assert response.status_code == HTTPStatus.CREATED
    response_content = response.json()
    assert response_content['summary'] == issue_summary_initial
    issue_id = response_content['id']
    changed_issue_summary = "Changed issue summary"
    response = client.post(
        f"issue/{issue_id}", json={"summary" : changed_issue_summary}
    )
    assert response.status_code == HTTPStatus.ACCEPTED
    response_content = response.json()
    assert response_content['issue_id'] == issue_id
    assert response_content['summary'] == changed_issue_summary