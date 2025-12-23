# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health, users, login

app = FastAPI(
    title="FastAPI Interview Challenge",
    version="1.0.0",
    description="API base para la prueba técnica."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    health.router, 
    prefix="/api", 
    tags=["Salud y Estatus"]
)


app.include_router(
    login.router, 
    prefix="/api",        
    tags=["Autenticación"]
)


app.include_router(
    users.router, 
    prefix="/api/users", 
    tags=["Usuarios"]
)


@app.get("/")
def root():
    return {"message": "FastAPI Interview Challenge is running 🎯"}

@app.on_event("startup")
async def startup_event():
    print("🚀 API iniciada")

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 API detenida")