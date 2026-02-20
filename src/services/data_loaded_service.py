from parser import WikiParser
from repo import CountryRepository
from sqlalchemy.ext.asyncio import AsyncSession


class DataLoadedService:
    def __init__(self, session: AsyncSession):
        self._repo = CountryRepository(session=session)
        self._parser = WikiParser()

    async def load(self):
        countries = await self._parser.parse_html()
        await self._repo.delete_all()
        await self._repo.save_all(countries)
