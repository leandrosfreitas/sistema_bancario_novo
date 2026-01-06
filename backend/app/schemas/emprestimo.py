from pydantic import BaseModel
from datetime import date
from uuid import UUID

class EmprestimoCreate(BaseModel):
    valor: float
    taxa_juros: float
    parcelas: int
    data_inicio: date
    conta_id: UUID

class EmprestimoOut(BaseModel):
    id: UUID
    valor: float
    taxa_juros: float
    parcelas: int
    data_inicio: date
    status: str
    conta_id: UUID

    class Config:
        from_attributes = True
