from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base_class import Base
from sqlalchemy import DateTime
from datetime import datetime

class Notificacao(Base):
    __tablename__ = "notificacoes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False)
    mensagem = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    data_envio = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pendente")
