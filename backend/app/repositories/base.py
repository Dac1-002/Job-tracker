from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository[T]:
    def __init__(self, model: type[T]):
        self.model = model

    async def get_by_id(
        self,
        db: AsyncSession,
        id: UUID,
        user_id: UUID,
    ) -> T | None:

        stmt = select(self.model).where(self.model.id == id)

        if hasattr(self.model, "user_id"):
            stmt = stmt.where(self.model.user_id == user_id)

        result = await db.execute(stmt)
        return result.scalars().first()

    async def list(
        self,
        db: AsyncSession,
        user_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> tuple[list[T], int]:

        stmt = select(self.model)
        count_stmt = select(func.count()).select_from(self.model)

        if hasattr(self.model, "user_id"):
            stmt = stmt.where(self.model.user_id == user_id)
            count_stmt = count_stmt.where(self.model.user_id == user_id)

        total = await db.execute(count_stmt)
        total = total.scalar()

        stmt = stmt.offset(skip).limit(limit)

        result = await db.execute(stmt)
        items = result.scalars().all()

        return items, total

    async def create(
        self,
        db: AsyncSession,
        obj_in: dict,
    ) -> T:

        obj = self.model(**obj_in)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    async def update(
        self,
        db: AsyncSession,
        db_obj: T,
        obj_in: dict,
    ) -> T:

        for key, value in obj_in.items():
            setattr(db_obj, key, value)

        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(
        self,
        db: AsyncSession,
        db_obj: T,
    ) -> None:

        await db.delete(db_obj)
        await db.commit()
