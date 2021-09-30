from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from typing import List, Tuple, Optional

import api.models.model as assignTodo_model
import api.schemas.assignTodo as assignTodo_schema



#post
async def add_assignTodo(db: AsyncSession, add_schema: assignTodo_schema.AssignTodoResponse)->assignTodo_model.AssignTodo:
    assignTodo = assignTodo_model.AssignTodo(todo_id=add_schema.todo_id, assignee_id=add_schema.assignee_id)

    db.add(assignTodo)
    await db.commit()
    await db.refresh(assignTodo)
    print(assignTodo.todo_assignee_id)
    return assignTodo


#get all assignTodos
async def get_all_assignTodos(db: AsyncSession)-> List[assignTodo_schema.AssignTodoResponse]:
	result: Result = await (
		db.execute(
			select(
				assignTodo_model.AssignTodo.todo_assignee_id,
				assignTodo_model.AssignTodo.todo_id,
				assignTodo_model.AssignTodo.assignee_id
			)
		)
	)

	return  result.all()

#get assignTodo of name:'name'
async def get_assignTodo(db: AsyncSession, todo_assignee_id:int)-> Optional[assignTodo_model.AssignTodo]:
		result: Result = await (
			db.execute(
				select(assignTodo_model.AssignTodo).filter(assignTodo_model.AssignTodo.todo_assignee_id == todo_assignee_id)
			)
		)

		assignTodo: Optional[Tuple[assignTodo_model.AssignTodo]] = result.first()

		return assignTodo[0] if assignTodo is not None else None

async def update_assignTodo(
		db: AsyncSession, assignTodo_schema: assignTodo_schema.AssignTodo, original:assignTodo_model.AssignTodo)-> assignTodo_model.AssignTodo:

		original.assignee_id = assignTodo_schema.assignee_id
		original.todo_id = assignTodo_schema.todo_id

		db.add(original)
		await db.commit()
		await db.refresh(original)
		return original


# delete by id
async def delete_assignTodo(delete_model:assignTodo_model.AssignTodo, db: AsyncSession) -> None:
		await db.delete(delete_model)
		await db.commit()
