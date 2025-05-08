# auth/routers/login.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.credentials_service import verify_user_credentials
from services.token_service import create_access_token

router = APIRouter()

class LoginInput(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login_user(data: LoginInput):
    user = await verify_user_credentials(data.email, data.password)
    token = create_access_token({"sub": str(user["user_id"])})
    return {"access_token": token, "token_type": "bearer"}
