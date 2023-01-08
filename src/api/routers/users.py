from fastapi import APIRouter

from api import crud
from common.database import schemas

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.User])
async def read_users() -> list[schemas.User]:
    return await crud.get_users()


@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    return await crud.create_user(user)
