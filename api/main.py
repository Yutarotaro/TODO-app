from fastapi import FastAPI
from routers import assignee, todo


app = FastAPI()

app.include_router(assignee.router)
app.include_router(todo.router)
app.include_router(assign-todo.router)

