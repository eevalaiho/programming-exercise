import sqlite3
import pytest

import modules
from modules.db import insert_scrapeItem
from modules.scrapeItem import scrapeItem


@pytest.mark.asyncio
async def test_insert_scrapeItem_None(mocker):
    mocker.patch.object(sqlite3, 'connect')  # sqlite3.connect
    await modules.db.insert_scrapeItem(None)
    sqlite3.connect.assert_not_called()


@pytest.mark.asyncio
async def test_insert_scrapeItem(mocker):
    mocker.patch.object(sqlite3, 'connect')
    item = scrapeItem('url', 200, 'pattern', [])
    await modules.db.insert_scrapeItem(item)
    sqlite3.connect.assert_called_once()