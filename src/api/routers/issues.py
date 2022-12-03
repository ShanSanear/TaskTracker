from http import HTTPStatus
from fastapi import APIRouter
from common.database.models import Issue

router = APIRouter(
    prefix="/issues",
    tags=["issues"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED, response_model=Issue)
async def create_issue(issue: Issue):
    obj = await Issue.objects.create(summary=issue.summary, description=issue.description)
    return obj


@router.patch("/{issue_id}", status_code=HTTPStatus.ACCEPTED, response_model=Issue)
async def change_issue(issue_id: int, issue: Issue):
    obj = await Issue.objects.get(id=issue_id)
    update_data = issue.dict(exclude_unset=True)
    await obj.update(**update_data)
    return obj
