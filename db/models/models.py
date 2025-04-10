from datetime import datetime

from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Integer,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from db.models.base import Base


class User(Base):
    __tablename__ = 'users'

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    reserves: Mapped[list["Reserve"]] = relationship(
        back_populates="user", lazy="selectin", cascade="all, delete-orphan"
    )

    def __str__(self):
        return (
            f'id: {self.tg_id}\n'
            f'username: {self.username}\n'
            f'name: {self.first_name}'
        )


class Reserve(Base):
    __tablename__ = 'reserves'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.tg_id'), nullable=False
    )
    customer_name: Mapped[str]
    time_reserve: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Связь с пользователем
    user: Mapped[User] = relationship(back_populates="reserves", lazy="joined")
