# auth/routers/login.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.credentials_service import verify_user_credentials, delete_user
from services.token_service import create_access_token, verify_token
from fastapi import APIRouter, Depends

router = APIRouter()

class LoginInput(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login_user(data: LoginInput):
    user = await verify_user_credentials(data.email, data.password)
    token = create_access_token({"sub": str(user["user_id"])})
    return {"access_token": token, "token_type": "bearer"}


@router.delete("/delete_auth/{user_id}")
async def remove_auth(user_id: int, payload: dict = Depends(verify_token)):
    return await delete_user(user_id)