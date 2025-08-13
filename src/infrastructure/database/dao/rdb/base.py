from typing import Generic, TypeVar

from pydantic import TypeAdapter
from sqlalchemy import delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm.strategy_options import Load

from infrastructure.database.models import BaseModel  # noqa

Model = TypeVar("Model", bound="BaseModel")


class BaseDAO(Generic[Model]):
    model: type[Model]

    def __init__(self, model: type[Model], session: AsyncSession):
        self.model: type[Model] = model
        self.session = session

    async def _get_all(
        self,
    ) -> list[Model]:
        result = await self.session.execute(select(self.model))
        adapter = TypeAdapter(list[Model])
        return adapter.validate_python(result.scalars().all())

    async def _get_by_id(
        self,
        id_: int,
        options: list[Load] | None = None,
    ) -> Model:
        query = select(self.model).where(self.model.id == id_)
        if options:
            query = query.options(*options)
        result = await self.session.execute(query)
        return result.scalar_one()

    def _save(
        self,
        obj: Model,
    ) -> None:
        self.session.add(obj)

    async def delete_all(
        self,
    ) -> None:
        await self.session.execute(delete(self.model))

    async def _delete(
        self,
        obj: Model,
    ) -> None:
        await self.session.delete(obj)

    async def count(
        self,
    ) -> int:
        result = await self.session.execute(select(func.count(self.model.id)))
        return result.scalar_one()

    async def commit(
        self,
    ) -> None:
        await self.session.commit()

    async def _flush(self, *objects: Model) -> None:
        await self.session.flush(objects)


__all__ = ["BaseDAO"]
