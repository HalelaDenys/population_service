from db import Country, db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, func, desc, asc
import asyncio


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

    async def get_region_stats(self):
        result = []
        regions = (
            (
                await self._session.execute(
                    select(self._model.region)
                    .group_by(self._model.region)
                    .order_by(self._model.region)
                )
            )
            .scalars()
            .all()
        )

        for region in regions:
            # population by region
            total_population = (
                await self._session.execute(
                    select(func.sum(self._model.population)).where(
                        self._model.region == region
                    )
                )
            ).scalar()

            # Country with the largest population
            max_row = (
                await self._session.execute(
                    select(self._model.country, self._model.population)
                    .where(self._model.region == region)
                    .order_by(desc(self._model.population))
                )
            ).first()
            max_country, max_pop = max_row

            # Country with the smallest population
            min_row = (
                await self._session.execute(
                    select(self._model.country, self._model.population)
                    .where(self._model.region == region)
                    .order_by(asc(self._model.population))
                )
            ).first()
            min_country, min_pop = min_row

            result.append(
                (
                    region,
                    int(total_population),
                    max_country,
                    max_pop,
                    min_country,
                    min_pop,
                )
            )

        return result
