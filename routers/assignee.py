from abc import get_cache_token
from fastapi import APIRouter, Depends, HTTPException
from typing import List,Tuple, Optional
import api.schemas.assignee as assignee_schema

from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.assignee as assignee_crud
from api.db import get_db

router = APIRouter(
	prefix="/assignee/v1",
	tags=["assignee/v1"],
	responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=List[assignee_schema.AssigneeResponse])
async def get_all_assignees(db: AsyncSession = Depends(get_db)):
	assignees = await assignee_crud.get_all_assignees(db)

	if assignees is None:
		raise HTTPException(status_code=422, detail="Assignees not found")
	
	return assignees


@router.get("/{assignee_id}", response_model=Optional[assignee_schema.AssigneeResponse])
async def get_assignee(assignee_id: int, db: AsyncSession = Depends(get_db)):
	assignee = await assignee_crud.get_assignee(db, assignee_id = assignee_id )

	if assignee is None:
		raise HTTPException(status_code=422, detail="Assignees not found")

	return assignee

@router.post("/", response_model=assignee_schema.AssigneeResponse)
async def add_assignee(assignee_body: assignee_schema.Assignee, db: AsyncSession = Depends(get_db)):
	assignee =  await assignee_crud.add_assignee(db, assignee_body)

	if assignee is None:
		raise HTTPException(status_code=404, detail="Input Assignee not registered")

	return assignee




@router.delete("/{assignee_id}", response_model=str)
async def delete_assignee(assignee_id:int , db: AsyncSession = Depends(get_db)):
	assignee = await assignee_crud.get_assignee(db, assignee_id = assignee_id)

	if assignee is None:
		raise HTTPException(status_code=404, detail="Assignee not found")

	await assignee_crud.delete_assignee(assignee, db)

	return "Successfully Deleted" 



@router.put("/{assignee_id}", response_model=assignee_schema.AssigneeResponse)
async def update_assignee(assignee_id: int, assignee_body: assignee_schema.Assignee, db: AsyncSession = Depends(get_db)):
	assignee = await assignee_crud.get_assignee(db, assignee_id=assignee_id)

	if assignee is None:
		raise HTTPException(status_code=404, detail="Assignee not found")

	return await assignee_crud.update_assignee(db, assignee_body, original=assignee)

