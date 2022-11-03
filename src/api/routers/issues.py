from http import HTTPStatus
from fastapi import APIRouter
from common.database.models import Issue

router = APIRouter(
    prefix="/issues",
    tags=["issues"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED)
async def create_issue(issue: Issue):
    obj = await Issue.objects.create(summary=issue.summary)
    return obj

@router.post("/<issue_id>", status_code=HTTPStatus.ACCEPTED)
async def change_issue(issue: Issue):
    obj = await Issue.objects.get(id=issue.id)
    await obj.update(summary=obj.summary)
    return obj


