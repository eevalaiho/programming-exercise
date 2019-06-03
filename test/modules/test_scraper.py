import asyncio
import aiohttp
import pytest

from modules.scraper import extract_content, fetch

"""
@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


def test_extract_content(event_loop):

    # Test match
    expected = ['dolor']
    assert expected == event_loop.run_until_complete(
        )

    # Test no match
    expected = []
    assert expected == event_loop.run_until_complete(
        extract_content('lorem ipsum <pre>dolor</pre> amet', '<title>([^<]*)</title>'))

"""

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