import os
import asyncio
from logging.config import fileConfig

from dotenv import load_dotenv
from alembic import context

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from app.db.base import Base

# IMPORTANT: force model imports so SQLAlchemy registers metadata
import app.db.models.user
import app.db.models.company
import app.db.models.application
import app.db.models.status_history
import app.db.models.contact
import app.db.models.document
import app.db.models.reminder


# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Alembic config
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_async_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    async def run():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

    asyncio.run(run())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()