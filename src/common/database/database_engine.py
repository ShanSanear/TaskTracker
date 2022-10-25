import databases
import ormar
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

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


engine = sqlalchemy.create_engine(settings.db_string)
metadata.create_all(engine)