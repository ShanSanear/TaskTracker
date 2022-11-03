from fastapi import APIRouter
from common.database.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users():
    return await User.objects.all()


@router.post("/")
async def create_user(user: User):
    obj = await User.objects.create(name=user.name, email=user.email)
    return obj
