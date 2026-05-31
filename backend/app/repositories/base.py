from typing import Generic, TypeVar, Type, Optional
from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    # -------------------------
    # GET BY ID (OWNERSHIP SAFE)
    # -------------------------
    async def get_by_id(
        self,
        db: AsyncSession,
        id: UUID,
        user_id: UUID,
    ) -> Optional[ModelType]:

        stmt = select(self.model).where(self.model.id == id)

        # enforce ownership if model supports it
        if hasattr(self.model, "user_id"):
            stmt = stmt.where(self.model.user_id == user_id)

        result = await db.execute(stmt)
        return result.scalars().first()

    # -------------------------
    # LIST (OWNERSHIP SAFE)
    # -------------------------
    async def list(
        self,
        db: AsyncSession,
        user_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> tuple[list[ModelType], int]:

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

    # -------------------------
    # CREATE
    # -------------------------
    async def create(
        self,
        db: AsyncSession,
        obj_in: dict,
    ) -> ModelType:

        obj = self.model(**obj_in)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    # -------------------------
    # UPDATE
    # -------------------------
    async def update(
        self,
        db: AsyncSession,
        db_obj: ModelType,
        obj_in: dict,
    ) -> ModelType:

        for key, value in obj_in.items():
            setattr(db_obj, key, value)

        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    # -------------------------
    # DELETE
    # -------------------------
    async def delete(
        self,
        db: AsyncSession,
        db_obj: ModelType,
    ) -> None:

        await db.delete(db_obj)
        await db.commit()