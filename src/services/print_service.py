from sqlalchemy.ext.asyncio import AsyncSession

from repo import CountryRepository


class PrintService:
    def __init__(self, session: AsyncSession):
        self._repo = CountryRepository(session=session)

    async def print_countries(self):
        status = await self._repo.get_region_stats()
        for row in status:
            region, total, max_country, max_pop, min_country, min_pop = row
            print(f"Назва регіону: {region}")
            print(f"Загальне населення регіону: {total}")
            print(f"Назва найбільшої країни в регіоні (за населенням): {max_country}")
            print(f"Населення найбільшої країни в регіоні: {max_pop}")
            print(f"Назва найменшої країни в регіоні: {min_country}")
            print(f"Населення найменшої країни в регіоні: {min_pop}")
            print("-" * 70)
