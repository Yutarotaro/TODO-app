from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from typing import List, Tuple, Optional

import api.models.model as assignee_model
import api.schemas.assignee as assignee_schema



#post
async def add_assignee(db: AsyncSession, add_schema: assignee_schema.AssigneeResponse)->assignee_model.Assignee:
    assignee = assignee_model.Assignee(name=add_schema.name, role=add_schema.role)
    db.add(assignee)
    await db.commit()
    await db.refresh(assignee)
    return assignee


#get all assignees
async def get_all_assignees(db: AsyncSession)-> List[assignee_schema.AssigneeResponse]:
	result: Result = await (
		db.execute(
			select(
				assignee_model.Assignee.assignee_id,
				assignee_model.Assignee.name,
				assignee_model.Assignee.role
			)
		)
	)

	return  result.all()

#get assignee of name:'name'
async def get_assignee(db: AsyncSession, assignee_id:int)-> Optional[assignee_model.Assignee]:
		result: Result = await (
			db.execute(
				select(assignee_model.Assignee).filter(assignee_model.Assignee.assignee_id == assignee_id)
			)
		)

		assignee: Optional[Tuple[assignee_model.Assignee]] = result.first()

		return assignee[0] if assignee is not None else None

async def update_assignee(
		db: AsyncSession, assignee_schema: assignee_schema.Assignee, original:assignee_model.Assignee)-> assignee_model.Assignee:

		original.name = assignee_schema.name
		original.role = assignee_schema.role

		db.add(original)
		await db.commit()
		await db.refresh(original)
		return original


# delete by id
async def delete_assignee(delete_model:assignee_model.Assignee, db: AsyncSession) -> None:
		await db.delete(delete_model)
		await db.commit()
