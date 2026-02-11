from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.modules.users.user_repository import get_user_by_id



router = APIRouter(prefix="/users",tags=["Users"])

@router.get("/me")
async def get_me (current_user = Depends(get_current_user)):
    user = await get_user_by_id(current_user["user_id"])
    return user