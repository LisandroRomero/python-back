from fastapi import APIRouter
from app.modules.auth.auth_schemas import LoginRequest,TokenResponse, RegisterRequest
from app.modules.auth.auth_controller import login_controller, register_controller

router = APIRouter(prefix="/auth" ,tags=["Auth"])

@router.post("/login",response_model=TokenResponse)
async def login (data:LoginRequest):
    return await login_controller(data)

@router.post("/register")
async def register(request: RegisterRequest):
    return await register_controller(request)
