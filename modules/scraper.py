import logging
import re
import asyncio, aiohttp

from modules import scrapeItem, db


@asyncio.coroutine
async def fetch(session, url):
    """
    Fetch content from a web request
    :param session: aiohttp.ClientSession()
    :param url: url
    :return: response.text()
    """
    async with session.get(url) as response:
        status = response.status
        text = await response.text()
    return (status, text)


@asyncio.coroutine
async def extract_content(str, pattern):
    """
    Extract content from a string using a regular expression pattern
    :param str: the content
    :param pattern: the pattern as string
    :return: a regular expression natches collection
    """
    return re.findall(re.compile(pattern), str)


@asyncio.coroutine
async def pull_urls(url_group, sleep_interval=3):
    """
    Fetch http reponse content from urls
    and parse it using a regular expression.
    Store in database.
    :param url_group: list of url's
    :param sleep_interval: interval to space out the requests in seconds, default 3
    :return:
    """
    # Fetch content
    async with aiohttp.ClientSession() as session:
        for url in url_group[1]:
            # Fetch html content
            try:
                (status, content) = await fetch(session, url)
                # Extract content using regex
                matches = await extract_content(content, url_group[0])
                # Insert db
                item = scrapeItem.scrapeItem(url, status, url_group[0], matches)
                await db.insert_scrapeItem(item)
                # Write log
                logging.info(item)
            except Exception as e:
                logging.info(str(e))

            await asyncio.sleep(sleep_interval)