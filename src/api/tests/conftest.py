import os

os.environ["DB_ENGINE"] = "sqlite"
from common.database.config import settings
import pytest as pytest

from common.database.models import BaseMeta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.db_string, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope='session')
def local_sqlite_dbn():
    BaseMeta.metadata.create_all(bind=engine)
    yield
    BaseMeta.metadata.drop_all(bind=engine)
