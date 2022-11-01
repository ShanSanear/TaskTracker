import logging
from pprint import pprint

from dynaconf import Dynaconf
logging.basicConfig(level=logging.DEBUG)
from pathlib import Path

settings = Dynaconf(
    settings_files=[Path(__file__).parent / "settings.toml"],
    envvar_prefix=False,
)

def get_db_string_from_settings():
    pprint(list(sorted(settings.items(), key=lambda x: x[0])))
    print(f"Settings: {settings.items()}", flush=True)
    return f"{settings.DB_ENGINE}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@" \
           f"{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.POSTGRES_DB}"


settings.db_string = get_db_string_from_settings()
