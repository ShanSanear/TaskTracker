import pytest as pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

os.environ["DB_ENGINE"] = "sqlite"
from common.database.config import settings

from common.database.models import BaseMeta

from ..main import api

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(settings.db_string, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(api)


@pytest.fixture()
def local_sqlite_dbn():
    BaseMeta.metadata.create_all(bind=engine)
    yield
    BaseMeta.metadata.drop_all(bind=engine)


def test_get_users(local_sqlite_dbn):
    new_account_name = "Name"
    new_account_email = "TestEmail@domain.com"
    response = client.post(
        "/users/", json={"name": new_account_name, "email": new_account_email}
    )
    assert response.status_code == 200, response.text

    response = client.get("/users/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert new_account_name in data[0]['name']
    assert new_account_email in data[0]['email']
