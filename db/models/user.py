from datetime import datetime

from sqlalchemy import BigInteger, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    reserves: Mapped[list["Reserve"]] = relationship(
        back_populates="user", lazy="selectin"
    )

    def __str__(self):
        return (
            f'id: {self.tg_id}\n'
            f'username: {self.username}\n'
            f'name: {self.first_name}'
        )


class Reserve(Base):
    __tablename__ = 'reserves'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    customer_name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user: Mapped[User] = relationship(back_populates="reserves", lazy="joined")
