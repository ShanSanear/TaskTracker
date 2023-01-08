from http import HTTPStatus
from fastapi import APIRouter
from api import crud
from common.database import schemas

router = APIRouter(
    prefix="/issues",
    tags=["issues"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED, response_model=schemas.Issue)
async def create_issue(issue: schemas.IssueCreate):
    obj = await crud.create_issue(issue)
    return obj


@router.patch("/{issue_id}", status_code=HTTPStatus.ACCEPTED, response_model=schemas.Issue)
async def change_issue(issue_id: int, issue: schemas.IssueChange):
    obj = await crud.change_issue(issue_id, issue)
    return obj
