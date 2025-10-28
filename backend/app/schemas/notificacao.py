from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Literal

class NotificacaoCreate(BaseModel):
    mensagem: str
    tipo: Literal["alerta", "informativo", "transacional"]
    usuario_id: UUID

class NotificacaoOut(BaseModel):
    id: UUID
    mensagem: str
    tipo: str
    status: str
    data_envio: datetime
    usuario_id: UUID

    class Config:
        from_attributes = True
