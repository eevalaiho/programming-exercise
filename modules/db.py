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
    if item is None:
        return

    conn = sqlite3.connect('./data/scraping.db')
    try:
        c = conn.cursor()
        sql = "INSERT INTO scrapeItem (scrape_time, url, status, pattern, matches) VALUES (?, ?, ?, ?, ?)"
        c.execute(sql, (item.time, item.url, item.status, item.pattern, str(item.matches)))
        conn.commit()
    except Exception as e:
        logging.error(str(e), item)

    conn.close()

