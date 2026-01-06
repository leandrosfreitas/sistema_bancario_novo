import uuid
from sqlalchemy import String, Float, Integer, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    valor: Mapped[float] = mapped_column(Float, nullable=False)
    parcelas: Mapped[int] = mapped_column(Integer, nullable=False)
    taxa_juros: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String, default="simulado")
    data_inicio: Mapped[str] = mapped_column(Date, nullable=False)

    conta_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("contas.id"),
        nullable=False
    )
