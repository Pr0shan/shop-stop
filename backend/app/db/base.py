from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import DateTime, String, func

Base = declarative_base()

class AuditBase(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    created_by: Mapped[str] = mapped_column(String, nullable=True)
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True
    )
    updated_by: Mapped[str] = mapped_column(String, nullable=True)

