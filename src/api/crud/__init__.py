from common.database import models, schemas
from common.database.schemas import UserCreate


async def get_users():
    return await models.User.objects.all()


async def create_user(user: UserCreate):
    return await models.User.objects.create(name=user.name, email=user.email, password=user.password)


async def create_issue(issue: schemas.Issue):
    return await models.Issue.objects.create(summary=issue.summary, description=issue.description)


async def change_issue(issue_id: int, issue: schemas.Issue):
    obj = await models.Issue.objects.get(id=issue_id)
    update_data = issue.dict(exclude_unset=True)
    await obj.update(**update_data)
    return obj
