from typing import Optional
from pydantic import BaseModel, Field

class AssignTodo(BaseModel):
	todo_id : int = Field(..., title="todo_id")
	assignee_id: int = Field(..., title="assignee_id")

class AssignTodoResponse(AssignTodo):
	todo_assignee_id: int

	class Config:
		orm_mode = True

