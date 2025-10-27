from sqlalchemy import Column, String, ForeignKey, Float, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base_class import Base

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conta_id = Column(UUID(as_uuid=True), ForeignKey("contas.id"), nullable=True)
    valor = Column(Float, nullable=False)
    codigo_barras = Column(String, nullable=False)
    data_vencimento = Column(Date, nullable=False)
    status = Column(String, default="pendente")
