import aiohttp
import pytest
#from pytest_mock import mocker

import modules
from modules.scraper import extract_content, fetch, pull_urls


@pytest.mark.asyncio
async def test_pull_urls_fetch(mocker):
    mocker.patch.object(modules.scraper, 'fetch')
    urls = ['https://github.com/eevalaiho']
    url_groups = ('<title>([^<]*)</title>', urls)
    await pull_urls(url_groups, sleep_interval=0) # Let's not sleep since we have only one url
    modules.scraper.fetch.assert_called_once()


@pytest.mark.asyncio
async def test_pull_urls_extract_content(mocker):
    mocker.patch.object(modules.scraper, 'extract_content')
    urls = ['https://github.com/eevalaiho']
    url_groups = ('<title>([^<]*)</title>', urls)
    result = await pull_urls(url_groups, sleep_interval=0) # Let's not sleep since we have only one url
    modules.scraper.extract_content.assert_called_once()


@pytest.mark.asyncio
async def test_extract_content_match():
    result = await extract_content('lorem <pre>ip</pre>sum <pre>dolor</pre> amet',
                                   '<pre>([^<]*)</pre>')
    assert ['ip', 'dolor'] == result
    assert 'ip' == result[0]


@pytest.mark.asyncio
async def test_extract_content_nomatch():
    result = await extract_content('lorem <pre>ip</pre>sum <pre>dolor</pre> amet',
                                   '<title>([^<]*)</title>')
    assert [] == result


@pytest.mark.asyncio
async def test_fetch_existing():
    session = aiohttp.ClientSession()
    result = await fetch(session, 'https://github.com/eevalaiho/')
    assert 200 == result[0]
    assert "<!DOCTYPE html>" in result[1]


@pytest.mark.asyncio
async def test_fetch_nonexisting():
    session = aiohttp.ClientSession()
    result = await fetch(session, 'https://github.com/eevalaiho/non-existing')
    assert 404 == result[0]