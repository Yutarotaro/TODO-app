from abc import get_cache_token
from fastapi import APIRouter, Depends, HTTPException
from typing import List,Tuple, Optional
import api.schemas.assignTodo as assignTodo_schema

from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.assignTodo as assignTodo_crud
import api.cruds.todo as todo_crud
import api.cruds.assignee as assignee_crud
from api.db import get_db

router = APIRouter(
	prefix="/v1/assign-todo",
	tags=["v1/assign-todo"],
	responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=List[assignTodo_schema.AssignTodoResponse])
async def get_all_assignTodos(db: AsyncSession = Depends(get_db)):
	assignTodos = await assignTodo_crud.get_all_assignTodos(db)

	if assignTodos is None:
		raise HTTPException(status_code=422, detail="No todo assigned")
	
	return assignTodos


@router.get("/{todo_assignee_id}", response_model=Optional[assignTodo_schema.AssignTodoResponse])
async def get_assignTodo(todo_assignee_id: int, db: AsyncSession = Depends(get_db)):
	assignTodo = await assignTodo_crud.get_assignTodo(db, todo_assignee_id = todo_assignee_id)

	if assignTodo is None:
		raise HTTPException(status_code=422, detail="assigned todo not found")

	return assignTodo

@router.post("/", response_model=assignTodo_schema.AssignTodoResponse)
async def add_assignTodo(assignTodo_body: assignTodo_schema.AssignTodo, db: AsyncSession = Depends(get_db)):
	todo = await todo_crud.get_todo(db, assignTodo_body.todo_id)
	if todo is None:
		raise HTTPException(status_code=404, detail=" todo not found")

	assignee = await assignee_crud.get_assignee(db, assignTodo_body.assignee_id)
	if assignee is None:
		raise HTTPException(status_code=404, detail=" assignee not found")


	assignTodo =  await assignTodo_crud.add_assignTodo(db, assignTodo_body)
	if assignTodo is None:
		raise HTTPException(status_code=404, detail="Input todo not assigned")

	return assignTodo




@router.delete("/{todo_assignee_id}", response_model=str)
async def delete_assignTodo(todo_assignee_id:int , db: AsyncSession = Depends(get_db)):
	assignTodo = await assignTodo_crud.get_assignTodo(db, todo_assignee_id = todo_assignee_id)

	if assignTodo is None:
		raise HTTPException(status_code=404, detail="Assigned todo not found")

	await assignTodo_crud.delete_assignTodo(assignTodo, db)

	return "Successfully Deleted" 



@router.put("/{todo_assignee_id}", response_model=assignTodo_schema.AssignTodoResponse)
async def update_assignTodo(todo_assignee_id: int, assignTodo_body: assignTodo_schema.AssignTodo, db: AsyncSession = Depends(get_db)):
	
	assignTodo = await assignTodo_crud.get_assignTodo(db, todo_assignee_id=todo_assignee_id)
	#assignTodo_idをもつtodo-assignee関係が存在しなければ、404
	if assignTodo is None:
		raise HTTPException(status_code=404, detail="Assignee not found")


	todo = await todo_crud.get_todo(db, assignTodo_body.todo_id)
	#todo_idをもつtodoが存在しなければ、404
	if todo is None:
		raise HTTPException(status_code=404, detail=" todo not found")

	assignee = await assignee_crud.get_assignee(db, assignTodo_body.assignee_id)
	#assignee_idをもつassigneeが存在しなければ、404
	if assignee is None:
		raise HTTPException(status_code=404, detail=" assignee not found")

	return await assignTodo_crud.update_assignTodo(db, assignTodo_body, original=assignTodo)

