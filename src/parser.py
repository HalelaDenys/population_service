import re
import aiohttp
from bs4 import BeautifulSoup
from config import HEADERS
from db import Country


class WikiParser:
    url = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959"

    async def fetch_html(self) -> str:
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.get(self.url) as resp:
                if resp.status == 200:
                    return await resp.text()
                else:
                    raise Exception(f"Failed to fetch page, status: {resp.status}")

    async def parse_html(self) -> list[Country]:
        html = await self.fetch_html()
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find(
            "table",
            {"class": "wikitable"},
        )
        rows = table.find_all("tr")[2:]

        results = []
        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 6:
                continue

            country = re.sub(r"\[\w*]", "", cols[0].get_text(strip=True))
            region = cols[4].get_text(strip=True)
            str_population = cols[2].get_text(strip=True).replace(",", "")

            try:
                population = int(str_population)
            except ValueError:
                continue

            results.append(
                Country(
                    country=country,
                    region=region,
                    population=population,
                )
            )
        return results
