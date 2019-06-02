import asyncio
import pytest

from scraper import scraper


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


def extract_content(event_loop): #extract_content(str, pattern):
    expected = 'dolor'
    assert expected == event_loop.run_until_complete(extract_content('lorem ipsum <pre>dolor</pre> amet'))