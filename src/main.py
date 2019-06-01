import asyncio
import scraper
import functools
import logging
import signal
import sys
from concurrent.futures import CancelledError


def shutdown():
    """Performs a clean shutdown"""
    logging.info('received stop signal')
    for task in asyncio.Task.all_tasks():
        logging.info(task)
        logging.info('cancelling task')
        task.cancel()


def supervisor(loop, urls):
    try:
        #while True:
        result = loop.run_until_complete(scraper.pull_urls(urls, functools.partial(shutdown)))
        logging.info(result)
    except CancelledError:
        logging.info('CancelledError')
    except KeyboardInterrupt:
        logging.info('KeyboardInterrupt')
    loop.close()
    sys.exit(1)


def main():
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Started")

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGHUP, functools.partial(shutdown, loop))
    loop.add_signal_handler(signal.SIGTERM, functools.partial(shutdown, loop))

    urls = (('<title>([^<]*)</title>', ['http://www.helsinki.fi', 'http://www.cgi.com']),
        ('<pre>([^<]*)</pre>', ['http://www.helsinki.fi',  'https://github.com/eevalaiho']),
        ('<media>([^<]*)</media>', ['http://www.cgi.com', 'https://github.com/eevalaiho']))

    urls = [('<title>([^<]*)</title>', ['http://www.helsinki.fi', 'http://www.cgi.com'])]

    supervisor(loop, urls)


if __name__ == '__main__':
    main()