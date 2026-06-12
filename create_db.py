import asyncio

from fastapi_zero.database import engine
from fastapi_zero.models import table_registry


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.create_all)


asyncio.run(main())
