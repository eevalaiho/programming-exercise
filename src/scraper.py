import logging
import re
import asyncio, aiohttp
import scrapeItem, db


@asyncio.coroutine
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


@asyncio.coroutine
async def extract_content(html, pattern):
    return re.findall(re.compile(pattern), html)


@asyncio.coroutine
async def pull_urls(url_group, sleep_interval=3):

    # Fetch content
    async with aiohttp.ClientSession() as session:
        for url in url_group[1]:
            # Fetch html content
            try:
                html = await fetch(session, url)
                # Extract content using regex
                content = await extract_content(html, url_group[0])
                # Insert db
                item = scrapeItem.ScrapeItem(url, url_group[0], str(content))
                await db.insert_scrapeItem(item)
                # Write log
                logging.info(str(item))
            except Exception as e:
                logging.info(str(e))

            await asyncio.sleep(sleep_interval)