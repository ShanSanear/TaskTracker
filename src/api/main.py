from fastapi import FastAPI

from common.database.database_engine import User, database

api = FastAPI()


@api.get("/")
def hello():
    return {"message": "Hello world!"}


@api.get("/users")
async def read_root():
    return await User.objects.all()


@api.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@api.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()