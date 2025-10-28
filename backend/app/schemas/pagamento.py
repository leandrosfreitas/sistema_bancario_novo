from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional

class PagamentoCreate(BaseModel):
    conta_id: UUID
    valor: float
    codigo_barras: str
    data_vencimento: date
    descricao: Optional[str] = None

class PagamentoOut(BaseModel):
    id: UUID
    conta_id: UUID
    valor: float
    codigo_barras: str
    data_vencimento: date
    status: str
    descricao: Optional[str] = None

    class Config:
        from_attributes = True
