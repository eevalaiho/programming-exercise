from datetime import datetime

from modules.scrapeItem import scrapeItem


def test_constructor():
    item = scrapeItem('url', 200, 'pattern', [])
    assert item.url == 'url'
    assert item.status == 200
    assert item.pattern == 'pattern'
    assert item.matches == []
    assert item.time < datetime.now()


def test_str():
    item = scrapeItem('url', 200, 'pattern', [])
    assert ': url, 200, pattern, matches: 0' in str(item)