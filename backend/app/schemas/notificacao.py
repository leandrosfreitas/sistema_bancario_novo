from pydantic import BaseModel
from datetime import datetime

class NotificacaoCreate(BaseModel):
    mensagem: str
    usuario_id: int

class NotificacaoOut(BaseModel):
    id: int
    mensagem: str
    data_envio: datetime
    usuario_id: int

    class Config:
        from_attributes = True
