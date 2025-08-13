from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from dto.user import User as DTOUser
from infrastructure.database.dao.rdb.base import BaseDAO
from infrastructure.database.models.user import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user_or_update(self, telegram_id: int, full_name: str, username: str | None = None) -> DTOUser:
        result = await self.session.execute(select(User).where(User.telegram_id == telegram_id))
        user = result.scalar()
        if user:
            user.full_name = full_name
            user.username = username or ""
        else:
            user = User(telegram_id=telegram_id, full_name=full_name, username=username)
            self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return DTOUser.model_validate(user)

    async def get_user_by_telegram_id(self, telegram_id: int) -> DTOUser | None:
        result = await self.session.execute(select(User).where(User.telegram_id == telegram_id))
        user = result.scalar()
        if user is not None:
            return DTOUser.model_validate(user)
        return None


__all__ = ["UserDAO"]
