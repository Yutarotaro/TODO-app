from sqlalchemy.sql.expression import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from typing import List, Tuple, Optional

import api.models.model as model
import api.schemas.assignee as assignee_schema
import api.schemas.todo as todo_schema
import api.schemas.assignTodo as assignTodo_schema




#get all assignees
async def get_all_todo_assignees(assignee_id, db: AsyncSession)-> List[int]:
	result: Result = await (
		db.execute(
			select(
				model.AssignTodo.todo_id
			).filter(model.AssignTodo.assignee_id ==  assignee_id)
		)
	)

	results = []
	for e in result.all():
		results.append(e[0])
	
	print(results)

	return results


async def get_all_todos_by_todo_id(todo_ids, db: AsyncSession)-> List[todo_schema.TodoResponse]:

	results:List[todo_schema.TodoResponse] = []

	for todo_id in todo_ids:
		result: Result = await (
			db.execute(
				select(
					model.Todo.todo_id,
					model.Todo.content,
					model.Todo.deadline,
					model.Todo.is_done,
					model.Todo.created_at,
					model.Todo.updated_at,
					model.Todo.deleted_at
				).filter(model.Todo.todo_id ==  todo_id)
			)
		)
		res = result.first()

		results.append(todo_schema.TodoResponse(todo_id=res.todo_id,
												content=res.content,
												deadline=res.deadline,
												is_done=res.is_done,
												created_at=res.created_at,
												updated_at=res.updated_at,
												deleted_at=res.deleted_at))

		print(results)

	return results
