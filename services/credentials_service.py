# auth/services/credentials_service.py
from database.mongodb import mongo
from passlib.hash import bcrypt
from fastapi import HTTPException
from utils.logger import logger
async def save_user_credentials(user_id:int, email: str, password: str):
    collection = mongo.db["credentials"]

    existing = await collection.find_one({"email": email})
    if existing:
        return  # Ya registrado

    await collection.insert_one({
        "user_id":user_id,
        "email": email,
        "password": password,
        "type": "citizen",
    })

async def verify_user_credentials(email: str, password: str):
    collection = mongo.db["credentials"]
    user = await collection.find_one({"email": email})
    logger.info(f"user retrieved{user}")
    if not user or password != user["password"]:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return user
