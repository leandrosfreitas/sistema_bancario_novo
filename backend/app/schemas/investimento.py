from pydantic import BaseModel
from datetime import date

class InvestimentoCreate(BaseModel):
    tipo: str
    valor: float
    data_aplicacao: date
    conta_id: int

class InvestimentoOut(BaseModel):
    id: int
    tipo: str
    valor: float
    data_aplicacao: date
    conta_id: int

    class Config:
        from_attributes = True
