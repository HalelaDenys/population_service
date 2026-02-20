from db import Country
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete


class CountryRepository:
    def __init__(self, session: AsyncSession):
        self._session = session
        self._model = Country

    async def delete_all(self) -> None:
        await self._session.execute(delete(self._model))
        await self._session.flush()

    async def save_all(self, countries: list[Country]) -> None:
        self._session.add_all(countries)
        await self._session.flush()
