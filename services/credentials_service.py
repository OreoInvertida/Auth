# auth/services/credentials_service.py
from database.mongodb import mongo
from passlib.hash import bcrypt
from fastapi import HTTPException

async def save_user_credentials(email: str, password: str):
    collection = mongo.db["credentials"]

    existing = await collection.find_one({"email": email})
    if existing:
        return  # Ya registrado

    await collection.insert_one({
        "email": email,
        "password": password
    })

async def verify_user_credentials(email: str, password: str):
    collection = mongo.db["credentials"]
    user = await collection.find_one({"email": email})
    if not user or not bcrypt.verify(password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return True
