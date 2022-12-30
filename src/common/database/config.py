import logging
from pprint import pprint

from dynaconf import Dynaconf
from pathlib import Path

settings = Dynaconf(
    settings_files=[Path(__file__).parent / "settings.toml"],
    envvar_prefix=False,
)

def get_db_string_from_settings():
    if settings.DB_ENGINE == "postgresql":
        return f"{settings.DB_ENGINE}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@" \
               f"{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.POSTGRES_DB}"
    elif settings.DB_ENGINE == "sqlite":
        # TODO - logging
        print("Getting sqlite test database")
        return "sqlite:///./test.db"
    raise ValueError(f"Unknown db_engine value: {settings.DB_ENGINE}")


settings.db_string = get_db_string_from_settings()