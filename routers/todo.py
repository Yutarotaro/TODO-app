from abc import get_cache_token
from fastapi import APIRouter, Depends, HTTPException
from typing import List,Tuple, Optional
import api.schemas.todo as todo_schema

from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.todo as todo_crud
from api.db import get_db

router = APIRouter(
	prefix="/todo/v1",
	tags=["todo/v1"],
	responses={404: {"description": "Not found"}}
)



@router.get("/", response_model=List[todo_schema.TodoResponse])
async def get_all_todos(db: AsyncSession = Depends(get_db)):
	todos = await todo_crud.get_all_todos(db)
	if todos is None:
		raise HTTPException(status_code=404, detail="Todos not found")
	
	return todos



@router.get("/{todo_id}", response_model=Optional[todo_schema.TodoResponse])
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
	todo = await todo_crud.get_todo(db, todo_id = todo_id )

	if todo is None:
		raise HTTPException(status_code=422, detail="Todos not found")

	return todo



@router.post("/", response_model=todo_schema.TodoResponse)
async def add_todo(todo_body: todo_schema.Todo, db: AsyncSession = Depends(get_db)):
	todo =  await todo_crud.add_todo(db, todo_body)

	if todo is None:
		raise HTTPException(status_code=404, detail="Todo not found")

	return todo




@router.delete("/{todo_id}", response_model=str)
async def delete_todo(todo_id:int , db: AsyncSession = Depends(get_db)):
	todo = await todo_crud.get_todo(db, todo_id = todo_id)

	if todo is None:
		raise HTTPException(status_code=404, detail="Todo not found")

	await todo_crud.delete_todo(todo, db)

	return "Successfully Deleted" 



@router.put("/{todo_id}", response_model=todo_schema.TodoResponse)
async def update_todo(todo_id: int, todo_body: todo_schema.Todo, db: AsyncSession = Depends(get_db)):
	todo = await todo_crud.get_todo(db, todo_id=todo_id)

	if todo is None:
		raise HTTPException(status_code=404, detail="Todo not found")

	print('OK')
	return await todo_crud.update_todo(db, todo_body, original=todo)


