from app.db.base import AuditBase
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(AuditBase):
    __tablename__ = "users"

    name: Mapped[str]
    email: Mapped[str]
    role: Mapped[str]

    #relationships
    owned_products: Mapped['Product'] = relationship(back_populates="owner")
    stocks: Mapped[list["Stock"]] = relationship(back_populates="seller")