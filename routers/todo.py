from fastapi import APIRouter

router = APIRouter()


#todo
@router.get("/todo")
async def todo():
	pass

@router.get("/todo/{task_id}")
async def todo():
	pass

@router.post("/todo")
async def todo():
	pass

@router.delete("/todo")
async def todo():
	pass

@router.put("/todo")
async def todo():
	pass


