from fastapi import FastAPI
from routers import assignee, todo, assignTodo, searchTodoByAssignee


app = FastAPI()

app.include_router(searchTodoByAssignee.router)
app.include_router(assignee.router)
app.include_router(todo.router)
app.include_router(assignTodo.router)

