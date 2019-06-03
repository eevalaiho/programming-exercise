import asyncio
import functools
import logging
import signal
import sys
from concurrent.futures import CancelledError

from modules import scraper


def shutdown(msg=""):
    """Performs a clean shutdown"""
    logging.info('Received stop signal: %s' % msg)
    for idx, task in enumerate(asyncio.Task.all_tasks()):
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

    # Url's to process
    urls = ['http://www.helsinki.fi', 'http://www.cgi.com',  'https://github.com/eevalaiho']
    url_groups = [('<title>([^<]*)</title>', urls),
                  ('(<link[^>]*>)', urls),
                  ('(UA\-[\w\d-]+)', urls)]

    # Setup logging
    logging.getLogger().setLevel(logging.INFO)

    # Setup async execution
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGHUP, functools.partial(shutdown, loop))
    loop.add_signal_handler(signal.SIGTERM, functools.partial(shutdown, loop))

    # Start the program
    supervisor(loop, url_groups)


if __name__ == '__main__':
    main()
