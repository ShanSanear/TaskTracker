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
    assert response_content["id"] == 1
    assert response_content["summary"] == issue_summary
    assert response_content["description"] is None


def test_create_issue_without_summary_should_raise_422(local_sqlite_dbn):
    response = client.post(
        "/issues/", json={"description" : "Test description"}
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_change_issue_summary(local_sqlite_dbn):
    issue_summary_initial = "Test issue summary"
    response = client.post(
        "/issues/", json={"summary": issue_summary_initial}
    )
    assert response.status_code == HTTPStatus.CREATED
    response_content = response.json()
    assert response_content['summary'] == issue_summary_initial
    changed_issue_summary = "Changed issue summary"
    issue_id = response_content['id']
    response = client.patch(
        f"/issues/{issue_id}", json={"summary": changed_issue_summary}
    )
    assert response.status_code == HTTPStatus.ACCEPTED
    response_content = response.json()
    assert response_content['id'] == issue_id
    assert response_content['summary'] == changed_issue_summary


def test_create_issue_with_description(local_sqlite_dbn):
    issue_summary_initial = "Test issue summary"
    issue_description_initial = "Test issue description"
    response = client.post(
        "/issues/", json={"summary": issue_summary_initial, "description": issue_description_initial}
    )
    assert response.status_code == HTTPStatus.CREATED
    response_content = response.json()
    assert response_content['summary'] == issue_summary_initial
    assert response_content['description'] == issue_description_initial
