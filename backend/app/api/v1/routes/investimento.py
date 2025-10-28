from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.investimento import InvestimentoCreate, InvestimentoOut
from app.models.investimento import Investimento
from app.models.conta import Conta
from app.db.session import get_db

router = APIRouter(prefix="/investimentos", tags=["Investimentos"])

@router.post("/", response_model=InvestimentoOut)
def aplicar_investimento(investimento: InvestimentoCreate, db: Session = Depends(get_db)):
    conta = db.query(Conta).get(investimento.conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    novo_investimento = Investimento(
        tipo=investimento.tipo,
        valor_aplicado=investimento.valor_aplicado,
        data_aplicacao=investimento.data_aplicacao,
        conta_id=investimento.conta_id,
        rentabilidade=0.0
    )

    db.add(novo_investimento)
    db.commit()
    db.refresh(novo_investimento)
    return novo_investimento
