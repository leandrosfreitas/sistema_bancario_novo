from pydantic import BaseModel
from datetime import date
from uuid import UUID

class InvestimentoCreate(BaseModel):
    tipo: str
    valor_aplicado: float
    data_aplicacao: date
    conta_id: UUID

class InvestimentoOut(BaseModel):
    id: UUID
    tipo: str
    valor_aplicado: float
    data_aplicacao: date
    rentabilidade: float
    conta_id: UUID

    class Config:
        from_attributes = True
