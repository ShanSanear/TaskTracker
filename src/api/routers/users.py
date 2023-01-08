from fastapi import APIRouter

from api import crud
from common.database.models import User
from common.database import schemas

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users() -> list[schemas.User]:
    return await crud.get_users()


@router.post("/",)
async def create_user(user: schemas.UserCreate):
    return await crud.create_user(user)
