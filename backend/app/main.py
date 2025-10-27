from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1 import api_router

app = FastAPI(
    title="Internet Banking API",
    debug=settings.DEBUG
)

# ✅ Middleware de CORS (permite comunicação com o frontend React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
