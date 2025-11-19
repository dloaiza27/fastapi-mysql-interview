from fastapi import APIRouter, Depends
from app.core.auth import verify_bearer_token
from app.core.database import test_db_connection

router = APIRouter()

@router.get("/health")
async def health_check(token: str = Depends(verify_bearer_token)):
    """
    Health check protegido con Bearer Token.
    TODO:
    - Validar conexión real a MySQL
    """
    db_ok = test_db_connection()
    return {"status": "ok", "db": db_ok}
