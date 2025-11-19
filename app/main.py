from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.users import router as users_router  # El candidato completará cuando implemente usuarios

app = FastAPI(
    title="FastAPI Interview Challenge",
    version="1.0.0",
    description="API base para la prueba técnica."
)

# Middleware CORS simple
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Se espera que el candidato pueda restringir esto si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(health_router, prefix="/api")
app.include_router(users_router, prefix="/api/users")  # El candidato debe activarlo

@app.get("/")
def root():
    """
    Endpoint raíz simple.
    Se espera que el candidato lo mantenga funcionando mientras hace cambios en otros routers.
    """
    return {"message": "FastAPI Interview Challenge is running 🎯"}

@app.on_event("startup")
async def startup_event():
    """
    Se espera que el candidato use este evento para preparar la DB o inicializar recursos.
    """
    print("🚀 API iniciada")

@app.on_event("shutdown")
async def shutdown_event():
    """
    Se espera que el candidato limpie recursos aquí si fuera necesario.
    """
    print("🛑 API detenida")
