import logging
import sqlite3
import asyncio


@asyncio.coroutine
async def insert_scrapeItem(item):
    """
    Insert scrapeItem in /data/scraping.db
    :param item: The item
    :return: void
    """
    conn = sqlite3.connect('../data/scraping.db')
    try:
        c = conn.cursor()
        sql = "INSERT INTO scrapeItem (scrape_time, url, pattern, content) VALUES (?, ?, ?, ?)"
        c.execute(sql, (item.time, item.url, item.pattern, item.content))
        conn.commit()
    except Exception as e:
        logging.error(str(e), item)

    conn.close()

