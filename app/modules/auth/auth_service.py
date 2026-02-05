import email
from fastapi import HTTPException
from app.infra.supabase_client import supabase
from app.core.security import create_acces_token, create_refresh_token
from app.modules.users.user_repository import create_user_profile

async def login_user(email:str, password:str):

    try:
        response = supabase.auth.sign_in_with_password({
            "email":email, 
            "password":password
            })
        if not response.user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )
        user_id = response.user.id

        access_token = create_acces_token({"sub": user_id})
        refresh_token = create_refresh_token({"sub":user_id})

        return {
            "access_token": access_token,
            "refresh_token":refresh_token
        }
    
    except Exception as e:
        raise HTTPException(
            status_code= 400,
            detail=str(e)
        )

async def register_user(email:str, password:str,full_name:str):


    try:

        auth_response = supabase.auth.sign_up({
            "email":email,
            "password": password
        })

        if not auth_response.user:
            raise HTTPException(
                status_code=400,
                detail="Error creating user"
            )
        user_id = auth_response.user.id

        await create_user_profile(user_id,email,full_name)

        access_token = create_acces_token({"sub": user_id})
        refresh_token = create_refresh_token({"sub":user_id})

        return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "token_type": "Bearer"
        }
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
