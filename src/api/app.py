from fastapi import FastAPI

from api.routers import users, issues,root

app = FastAPI()
app.include_router(users.router)
app.include_router(issues.router)
app.include_router(root.router)

