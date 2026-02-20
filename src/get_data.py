import asyncio
from db import db_helper, Base
from services import DataLoadedService


async def main():
    await db_helper.create_tables(base=Base)

    async with db_helper.get_session() as session:
        load_service = DataLoadedService(session=session)
        await load_service.load()
        print("Data loaded")


if __name__ == "__main__":
    asyncio.run(main())
