from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import api_router
from app.middlewares.cors import setup_cors

app = FastAPI(
    title="Internet Banking API",
    debug=settings.DEBUG
)

setup_cors(app)

# ✅ Rotas da API
app.include_router(api_router, prefix="/api/v1")

# ✅ Eventos de inicialização
@app.on_event("startup")
async def startup_event():
    print("🚀 Servidor iniciado com sucesso!")

# ✅ Eventos de encerramento
@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 Servidor encerrado.")
