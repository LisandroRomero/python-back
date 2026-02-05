from app.modules.auth.auth_service import login_user, register_user
from app.modules.auth.auth_schemas import RegisterRequest

async def login_controller(data):
    return await login_user(data.email, data.password)


async def register_controller (request: RegisterRequest):
    return await register_user(
        request.email,
        request.password,
        request.full_name
    )
        
    