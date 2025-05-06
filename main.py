# auth/main.py
from fastapi import FastAPI
from database.mongodb import mongo
from routers.validate import router as validate_router

app = FastAPI(title="Auth Microservice")

@app.on_event("startup")
async def startup_db():
    await mongo.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await mongo.close()


app.include_router(validate_router, prefix="/auth", tags=["Validation"])