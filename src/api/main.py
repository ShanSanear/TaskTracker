from fastapi import FastAPI

from common.database.models import User, database

api = FastAPI()

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

@api.get("/users/")
async def read_users():
    return await User.objects.all()

@api.post("/users/")
async def create_user(user: User):
    obj = await User.objects.create(name=user.name, email=user.email)
    return obj

