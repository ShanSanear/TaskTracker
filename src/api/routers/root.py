import os

from fastapi import APIRouter

from common.database import models

router = APIRouter(
    prefix="",
    tags=["manage", "root"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
def hello():
    return {"message": "Hello world!"}


@router.on_event("startup")
async def startup():
    print("App startup")
    if not models.database.is_connected:
        await models.database.connect()
    await models.database.connect()
    if os.getenv("DEBUG_MODE") == 'true':
        print(f"Create all in test, {models.BaseMeta.metadata.tables}")
        models.BaseMeta.metadata.create_all(bind=models.engine)
        await models.User.objects.get_or_create(name="Name", email="TestEmail@domain.com")


@router.on_event("shutdown")
async def shutdown():
    if models.database.is_connected:
        if os.getenv("DEBUG_MODE") == 'true':
            models.BaseMeta.metadata.drop_all(bind=models.engine)
        await models.database.disconnect()
