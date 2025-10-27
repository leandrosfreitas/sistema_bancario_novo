from pydantic import BaseModel
from datetime import date

class EmprestimoCreate(BaseModel):
    valor: float
    juros: float
    parcelas: int
    data_inicio: date
    conta_id: int

class EmprestimoOut(BaseModel):
    id: int
    valor: float
    juros: float
    parcelas: int
    data_inicio: date
    conta_id: int

    class Config:
        from_attributes = True
