from fastapi import APIRouter
from app.api.v1.routes import usuario, conta, transacao, perfil, auth, cartao, emprestimo, pagamento, notificacao, investimento, login

api_router = APIRouter()
api_router.include_router(usuario.router)
api_router.include_router(conta.router)
api_router.include_router(pagamento.router)
api_router.include_router(transacao.router)
api_router.include_router(cartao.router)
api_router.include_router(emprestimo.router)
api_router.include_router(auth.router)
api_router.include_router(perfil.router)
api_router.include_router(notificacao.router)
api_router.include_router(investimento.router)
