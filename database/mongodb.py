# auth/database/mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

#load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://oreo:negronauta@authentication.nppj2o.mongodb.net/?retryWrites=true&w=majority&appName=Authentication")
DB_NAME = os.getenv("AUTH_DB_NAME", "auth_db")

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        print("Conectado a MongoDB (AUTH)")

    async def close(self):
        self.client.close()
        print("🔌 Conexión MongoDB cerrada")

mongo = MongoDB()
