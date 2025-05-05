# auth/main.py
from fastapi import FastAPI
from routers.validate import router as validate_router

app = FastAPI(title="Auth Microservice")

app.include_router(validate_router, prefix="/auth", tags=["Validation"])
