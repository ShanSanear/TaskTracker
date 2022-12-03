import ormar

import databases
import sqlalchemy

from common.database.config import settings

database = databases.Database(settings.db_string)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id = ormar.Integer(primary_key=True)  # TODO Integer to UUID
    name = ormar.String(max_length=128, unique=True, nullable=False, )
    email = ormar.String(max_length=128, unique=True, )
    active = ormar.Boolean(default=True, nullable=False)


class Issue(ormar.Model):
    class Meta(BaseMeta):
        tablename = "issue"

    id = ormar.Integer(primary_key=True)
    summary = ormar.String(max_length=256, nullable=False)
    description = ormar.String(max_length=10000, nullable=True)


engine = sqlalchemy.create_engine(settings.db_string)
