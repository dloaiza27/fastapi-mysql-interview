from fastapi import APIRouter, Depends
from app.core.auth import verify_bearer_token
from app.core.database import test_db_connection

router = APIRouter()

@router.get("/healthy")
async def health_check():
    """
    **Aquí tu reto es adaptar esta API incluyendo buenas prácticas 
    para el manejo de la respuesta de la API.
    """
    db_ok = test_db_connection()
    return {"status": "ok", "db": db_ok}
