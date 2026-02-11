from fastapi import responses
from app.infra.supabase_client import supabase

async def create_user_profile(user_id: str,email:str,full_name:str):
    data = {
        "id" : user_id,
        "email": email,
        "full_name":full_name
    }

    response = supabase.table("users").insert(data).execute()
    return  response


async def get_user_by_id(user_id:str):
    response= supabase.table("users").select("*").eq("id",user_id).single().execute()
    if not response.data:
        raise Exception("user_not_found")
        

    return response.data