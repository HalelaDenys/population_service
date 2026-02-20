import asyncio
from db import db_helper
from services import PrintService


async def main():

    async with db_helper.get_session() as session:
        print_service = PrintService(session=session)
        await print_service.print_countries()


if __name__ == "__main__":
    asyncio.run(main())
