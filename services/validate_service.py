# auth/services/validate_service.py
import httpx
from fastapi import HTTPException
from utils.logger import logger
from dotenv import load_dotenv
import os

load_dotenv()

REGISTRADURIA_API = os.getenv("REGISTRADURIA_API")

async def validate_citizen(citizen_id: int):
    url = f"{REGISTRADURIA_API}/validateCitizen/{citizen_id}"
    logger.info(f"→ Validando ciudadano con ID: {citizen_id}")
    logger.info(f"→ Consultando URL: {url}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            logger.info(f"← Código de respuesta: {response.status_code}")

            if response.status_code == 200:
                return {"status": "registered"}
            elif response.status_code == 204:
                return {"status": "not_registered"}
            elif response.status_code in [500, 501]:
                logger.error(f"Error en API externa: {response.text}")
                raise HTTPException(
                    status_code=502,
                    detail="Error desde API de Registraduría"
                )
            else:
                logger.warning("⚠️ Respuesta inesperada.")
                raise HTTPException(status_code=500, detail="Respuesta inesperada")

        except httpx.RequestError as e:
            logger.error(f"Error de conexión: {e}")
            raise HTTPException(status_code=503, detail=str(e))
