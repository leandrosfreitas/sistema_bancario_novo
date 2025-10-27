from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base_class import Base

class Investimento(Base):
    __tablename__ = "investimentos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tipo = Column(String, nullable=False)
    valor_aplicado = Column(Float, nullable=False)
    rentabilidade = Column(Float, default=0.0)
    conta_id = Column(UUID(as_uuid=True), ForeignKey("contas.id"), nullable=False)
