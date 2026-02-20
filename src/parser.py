import aiohttp
from bs4 import BeautifulSoup

from db import Country


class WikiParser:
    url = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959"

    async def fetch_html(self) -> str:
        headers = {
            "User-Agent": "MyProject/1.0 (+https://example.com/contact; email: your_email@example.com)",
        }
        async with aiohttp.ClientSession(headers=headers) as session:
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

            country = cols[0].text.strip()
            region = cols[4].text.strip()
            str_population = cols[2].text.strip().replace(",", "")

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
