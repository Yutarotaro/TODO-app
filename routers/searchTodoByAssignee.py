from abc import get_cache_token

from sqlalchemy.sql.expression import null
from fastapi import APIRouter, Depends, HTTPException
from typing import List,Tuple, Optional
import api.schemas.todo as todo_schema
import api.schemas.assignee as assignee_schema

from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.searchTodoByAssignee as search_crud
import api.cruds.assignee as assignee_crud
from api.db import get_db

router = APIRouter(
	prefix="/v1/search",
	tags=["v1/search"],
	responses={404: {"description": "Not found"}}
)


@router.get("/{assignee_id}", response_model=List[todo_schema.TodoResponse])
async def get_todos_by_assignee(assignee_id: int, db: AsyncSession = Depends(get_db)):

	assignee:assignee_schema = await assignee_crud.get_assignee(db, assignee_id = assignee_id)

	#assignee_idを持つassigneeがいなければ、404
	if assignee is None:
		raise HTTPException(status_code=404, detail="Assignee not found")
	

	todo_ids:List[int] = await search_crud.get_all_todo_assignees(assignee_id, db)

	#assignee_idに紐づいたtodoがなければ、404
	if todo_ids is None:
		raise HTTPException(status_code=404, detail=f"Todo of assignee_id {assignee_id} not found")
	

	todos:List[todo_schema.TodoResponse] = await search_crud.get_all_todos_by_todo_id(todo_ids, db)

	return todos
