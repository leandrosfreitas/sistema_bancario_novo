from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.notificacao import NotificacaoCreate, NotificacaoOut
from app.models.notificacao import Notificacao
from app.models.usuario import Usuario
from app.db.session import get_db

router = APIRouter(prefix="/notificacoes", tags=["Notificações"])

@router.post("/", response_model=NotificacaoOut)
def enviar_notificacao(notificacao: NotificacaoCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).get(notificacao.usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    nova_notificacao = Notificacao(
        mensagem=notificacao.mensagem,
        tipo=notificacao.tipo,
        usuario_id=notificacao.usuario_id,
        status="pendente"
    )

    db.add(nova_notificacao)
    db.commit()
    db.refresh(nova_notificacao)
    return nova_notificacao
