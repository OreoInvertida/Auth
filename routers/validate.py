from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.validate_service import validate_citizen
from services.credentials_service import save_user_credentials
from fastapi.responses import JSONResponse
from fastapi import Response

router = APIRouter()

class ValidationInput(BaseModel):
    id: int
    email: str
    password: str

# Validación simple de seguridad de contraseña
def validate_password_strength(password: str) -> bool:
    import re
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return True
    return False




@router.post("/validate")
async def validate_user(data: ValidationInput):
    # Validar ID
    print(data.id)
    if len(str(data.id)) < 10:
        raise HTTPException(
            status_code=421,
            detail="El número de identificación debe tener al menos 10 dígitos."
        )

    # Validar contraseña
    if not validate_password_strength(data.password):
        raise HTTPException(
            status_code=422,
            detail="La contraseña no es segura. Debe tener al menos 8 caracteres, mayúsculas, minúsculas, un número y un símbolo."
        )

    result = await validate_citizen(data.id)

    if result["status"] == "registered":
        return JSONResponse(status_code=200, content=result)
    elif result["status"] == "not_registered":
        await save_user_credentials(data.id,data.email, data.password)
        return Response(status_code=204)


