from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.dao.rdb.base import BaseDAO
from infrastructure.database.dao.rdb.user import UserDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseDAO
        self.user = UserDAO(self.session)


__all__ = ["HolderDao"]
