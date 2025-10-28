from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.transacao import TransacaoCreate, TransacaoOut
from app.models.transacao import Transacao
from app.models.conta import Conta
from app.db.session import get_db

router = APIRouter(prefix="/transacoes", tags=["Transações"])

@router.post("/", response_model=TransacaoOut)
def realizar_transacao(transacao: TransacaoCreate, db: Session = Depends(get_db)):
    conta = db.query(Conta).get(transacao.conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if transacao.tipo == "saque" and conta.saldo < transacao.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    if transacao.tipo == "saque":
        conta.saldo -= transacao.valor
    elif transacao.tipo == "deposito":
        conta.saldo += transacao.valor
    else:
        raise HTTPException(status_code=400, detail="Tipo de transação inválido")

    nova_transacao = Transacao(
        valor=transacao.valor,
        tipo=transacao.tipo,
        descricao=transacao.descricao,
        conta_id=transacao.conta_id,
        status="concluída"
    )

    db.add(nova_transacao)
    db.add(conta)  # garante que o saldo atualizado será salvo
    db.commit()
    db.refresh(nova_transacao)
    return nova_transacao
