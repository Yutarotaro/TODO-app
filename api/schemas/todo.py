from typing import Optional
from pydantic import BaseModel, Field
import datetime

class Todo(BaseModel):
	content: str = Field(...)
	deadline: datetime.datetime = Field(...)
	is_done: bool = Field(False)
	created_at: Optional[datetime.datetime] = Field(...)
	updated_at: Optional[datetime.datetime] = Field(datetime.datetime.now())
	deleted_at: Optional[datetime.datetime] = Field(...)

class TodoResponse(Todo):
	todo_id: int

	class Config:
		orm_mode = True

