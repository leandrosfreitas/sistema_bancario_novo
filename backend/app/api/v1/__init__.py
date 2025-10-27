from fastapi import APIRouter
from app.api.v1.routes import usuario, conta

api_router = APIRouter()
api_router.include_router(usuario.router)
api_router.include_router(conta.router)
