import asyncio
import functools
import logging
import signal
import sys
from concurrent.futures import CancelledError

from scraper import scraper

def shutdown(msg=""):
    """Performs a clean shutdown"""
    logging.info('Received stop signal: %s' % msg)
    for idx, task in enumerate(asyncio.Task.all_tasks()):
        #logging.info(task)
        logging.info('Cancelling task %s' % idx)
        task.cancel()


def supervisor(loop, url_groups):
    try:
        tasks = []
        # Make one batch of each url group
        for group in url_groups:
            tasks.append(asyncio.ensure_future(scraper.pull_urls(group)))
        # Execute tasks
        loop.run_until_complete(asyncio.gather(*tasks))
    except CancelledError:
        shutdown("CancelledError")
    except KeyboardInterrupt:
        shutdown("KeyboardInterrupt")
    loop.close()
    sys.exit(1)


def main():
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Started")

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGHUP, functools.partial(shutdown, loop))
    loop.add_signal_handler(signal.SIGTERM, functools.partial(shutdown, loop))

    url_groups = [('<title>([^<]*)</title>', ['http://www.helsinki.fi', 'http://www.cgi.com']),
        ('<pre>([^<]*)</pre>', ['http://www.helsinki.fi',  'https://github.com/eevalaiho']),
        ('<media>([^<]*)</media>', ['http://www.cgi.com', 'https://github.com/eevalaiho'])]

    supervisor(loop, url_groups)


if __name__ == '__main__':
    main()