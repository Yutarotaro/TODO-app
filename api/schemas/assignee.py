from typing import Optional
from pydantic import BaseModel, Field

class Assignee(BaseModel):
	id: Optional[int] = Field(..., title="assignee_id")
	name: str = Field(..., title="assignee_name")
	role: str = Field(..., title="assignee_role")

