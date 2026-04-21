import enum

from sqlalchemy import ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import AuditBase

class StockStatus(str, enum.Enum):
    ACTIVE = "active"
    REMOVE = "remove"

class Stock(AuditBase):
    __tablename__ = "stocks"

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    price: Mapped[float] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(default=0)

    status: Mapped[StockStatus] = mapped_column(
        Enum(StockStatus),
        default=StockStatus.ACTIVE,
        nullable=False
    )

    #relationships
    product: Mapped["Product"] = relationship(back_populates="stocks")
    seller: Mapped["User"] = relationship(back_populates="stocks")

    __table_args__ = (
        UniqueConstraint("product_id", "seller_id", name="uix_product_seller"),
    )