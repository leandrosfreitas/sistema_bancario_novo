from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.pagamento import PagamentoCreate, PagamentoOut
from app.models.pagamento import Pagamento
from app.models.conta import Conta
from app.db.session import get_db

router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])

@router.post("/", response_model=PagamentoOut)
def criar_pagamento(pagamento: PagamentoCreate, db: Session = Depends(get_db)):
    conta = db.query(Conta).get(pagamento.conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    novo_pagamento = Pagamento(
        conta_id=pagamento.conta_id,
        valor=pagamento.valor,
        codigo_barras=pagamento.codigo_barras,
        data_vencimento=pagamento.data_vencimento,
        descricao=pagamento.descricao,
        status="pendente"
    )

    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)
    return novo_pagamento
