from pydantic import BaseModel
from datetime import date

class PagamentoCreate(BaseModel):
    descricao: str
    valor: float
    data_pagamento: date
    conta_id: int

class PagamentoOut(BaseModel):
    id: int
    descricao: str
    valor: float
    data_pagamento: date
    conta_id: int

    class Config:
        from_attributes = True
