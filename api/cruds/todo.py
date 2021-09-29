from datetime import datetime
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from typing import List, Tuple, Optional

import api.models.model as todo_model
import api.schemas.todo as todo_schema
from sqlalchemy.sql.type_api import NULLTYPE



#post
async def add_todo(db: AsyncSession, add_schema: todo_schema.TodoResponse)->todo_model.Todo:
    todo = todo_model.Todo(
		content=add_schema.content,
		deadline=add_schema.deadline,
		is_done=add_schema.is_done,
		created_at=add_schema.created_at,
		updated_at=add_schema.updated_at,
		deleted_at=add_schema.deleted_at
		)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


#get all todos
async def get_all_todos(db: AsyncSession)-> List[todo_schema.TodoResponse]:
	result: Result = await (
		db.execute(
			select(
				todo_model.Todo.todo_id,
				todo_model.Todo.content,
				todo_model.Todo.deadline,
				todo_model.Todo.is_done,
				todo_model.Todo.created_at,
				todo_model.Todo.updated_at,
				todo_model.Todo.deleted_at,
			)
		)
	)

	return  result.all()

async def get_todo(db: AsyncSession, todo_id:int)-> Optional[todo_model.Todo]:
	result: Result = await (
		db.execute(
			select(todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id)
		)
	)

	todo: Optional[Tuple[todo_model.Todo]] = result.first()

	return todo[0] if todo is not None else None

async def update_todo(
	db: AsyncSession, todo_schema: todo_schema.Todo, original:todo_model.Todo)-> todo_model.Todo:

	if (not original.is_done) and todo_schema.is_done:    #終了したとき
		original.deleted_at = datetime.now()
	elif original.is_done and (not todo_schema.is_done):  #終了を取り消すとき
		original.deleted_at = null

	original.content = todo_schema.content if todo_schema.content else original.content
	original.deadline = todo_schema.deadline if todo_schema.deadline else original.deadline
	original.is_done = todo_schema.is_done if todo_schema.is_done else original.is_done
	original.created_at = todo_schema.created_at if todo_schema.created_at else original.created_at
	original.updated_at = datetime.now()

	db.add(original)
	await db.commit()
	await db.refresh(original)
	return original


# delete by id
async def delete_todo(delete_model:todo_model.Todo, db: AsyncSession) -> None:
		await db.delete(delete_model)
		await db.commit()
