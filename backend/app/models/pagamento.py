import uuid
from sqlalchemy import String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    conta_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("contas.id"),
        nullable=True
    )

    descricao: Mapped[str | None] = mapped_column(String, nullable=True)
    valor: Mapped[float] = mapped_column(Float, nullable=False)
    codigo_barras: Mapped[str] = mapped_column(String, nullable=False)
    data_vencimento: Mapped[str] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String, default="pendente")
