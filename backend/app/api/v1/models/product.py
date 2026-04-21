from app.db.base import AuditBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey
import enum

class ProductStatus(str, enum.Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    ARCHIVED = "archived"

class Product(AuditBase):
    __tablename__ = "products"

    slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    owner_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    status: Mapped[ProductStatus] = mapped_column(
        Enum(ProductStatus),
        default=ProductStatus.ACTIVE,
        nullable=False
    )

    #relationships
    owner: Mapped["User"] = relationship(back_populates="owned_products")
    stocks: Mapped[list["Stock"]] = relationship(back_populates="product")

