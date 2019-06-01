import logging
import sqlite3
import asyncio

@asyncio.coroutine
async def insert_item(item):
    print(item)
    conn = sqlite3.connect('../data/scraping.db')
    try:
        c = conn.cursor()
        sql = "INSERT INTO web_items (scrape_time, url, pattern, content) VALUES (?, ?, ?, ?)"
        c.execute(sql, item)
        conn.commit()
    except Exception as e:
        logging.info(str(e))

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

    #return True