from sqlalchemy.ext.asyncio import AsyncSession

from db.models.models import User


async def create_user(
    session: AsyncSession, tg_id: int, first_name: str, last_name: str | None
) -> User:
    """Создает нового пользователя в БД."""
    user = User(tg_id=tg_id, first_name=first_name, last_name=last_name)
    session.add(user)
    await session.commit()
    return user


async def create_or_update_user(
    session: AsyncSession,
    tg_id: int,
    first_name: str,
    last_name: str | None = None,
    username: str | None = None,
) -> tuple[User, dict]:
    """
    Создает пользователя в бд или изменят данные о нём, если он уже существует.

    Parameters:
        session (AsyncSession): Сессия базы данных.
        tg_id (int): Telegram ID пользователя.
        first_name (str): Имя пользователя.
        last_name (str | None): Фамилия пользователя, по умолчанию None.
        username (str | None): Username пользователя в телеграм.

    Returns:
        Tuple[Union[User, None], Dict[str, bool]]: Кортеж с пользователем и
        информацией об операции (created и updated).
    """
    user: User | None = await session.get(User, tg_id)
    info = {'created': False, 'updated': False}

    if not user:
        user = await create_user(session, tg_id, first_name, last_name)
        info['created'] = True

    else:
        if user.first_name != first_name:
            user.first_name = first_name
            info['updated'] = True

        if user.last_name != last_name:
            user.last_name = last_name
            info['updated'] = True

        if user.username != username:
            user.username = username
            info['updated'] = True

        if info['updated']:
            await session.commit()

    return user, info
