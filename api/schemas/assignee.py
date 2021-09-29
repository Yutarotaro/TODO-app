from typing import Optional
from pydantic import BaseModel, Field

class Assignee(BaseModel):
	name: str = Field(..., title="assignee_name")
	role: str = Field(..., title="assignee_role")

class AssigneeResponse(Assignee):
	assignee_id: int

	class Config:
		orm_mode = True

