import re
import asyncio
import aiohttp
import logging


@asyncio.coroutine
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


@asyncio.coroutine
async def extract_content(html, pattern):
    return re.findall(re.compile(pattern), html)


@asyncio.coroutine
async def pull_urls(patterns, shutdown):

    # Fetch content
    async with aiohttp.ClientSession() as session:
        for idx, pattern in enumerate(patterns):
            logging.info("%s: %s" % (idx, pattern[0]))
            for jdx, url in enumerate(pattern[1]):
                logging.info("%s: %s" % (jdx, url))
                # Fetch html content
                try:
                    html = await fetch(session, url)
                    # Extract content using regex
                    content = await extract_content(html, pattern[0])
                    logging.info(content)
                    await asyncio.sleep(3)
                except Exception as e:
                    logging.info(str(e))
    shutdown()
