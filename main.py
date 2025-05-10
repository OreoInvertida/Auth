# auth/main.py
from fastapi import FastAPI
from database.mongodb import mongo
from routers.validate import router as validate_router
from routers.login import router as login_router


app = FastAPI(title="Auth Microservice", docs_url="/auth/docs", redoc_url="/redoc", openapi_url="/auth/openapi.json")

@app.on_event("startup")
async def startup_db():
    await mongo.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await mongo.close()


app.include_router(validate_router, tags=["Validation"])
app.include_router(login_router,tags=["Login"])