from fastapi import FastAPI

from common.database.models import User, database

from .routers import users, issues

api = FastAPI()
api.include_router(users.router)
api.include_router(issues.router)

@api.get("/")
def hello():
    return {"message": "Hello world!"}


@api.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    await database.connect()
    await User.objects.get_or_create(name="Name", email="TestEmail@domain.com")


@api.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
