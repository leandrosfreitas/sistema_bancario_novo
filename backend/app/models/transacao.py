from sqlalchemy import Column, ForeignKey, Float, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base_class import Base

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conta_origem_id = Column(UUID(as_uuid=True), ForeignKey("contas.id"), nullable=False)
    conta_destino_id = Column(UUID(as_uuid=True), ForeignKey("contas.id"), nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)
    status = Column(String, default="pendente")
    data = Column(DateTime, default=datetime.utcnow)
