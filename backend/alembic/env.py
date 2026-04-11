import os
import asyncio
from logging.config import fileConfig

from dotenv import load_dotenv
from alembic import context

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from app.db.base import Base

# IMPORTANT: load .env reliably (fixes path issues)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

DATABASE_URL = os.getenv("DATABASE_URL")

# Debug (you can remove later)
print("DATABASE_URL =", DATABASE_URL)

config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# IMPORTANT: this is what Alembic uses for autogenerate
target_metadata = Base.metadata


# -------------------------
# OFFLINE MODE
# -------------------------
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# -------------------------
# ONLINE MODE (ASYNC)
# -------------------------
def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
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


# -------------------------
# ENTRY POINT
# -------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()