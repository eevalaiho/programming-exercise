import asyncio
import logging

import app


def test_main(mocker):
    mocker.patch.object(logging, 'getLogger')
    mocker.patch.object(asyncio, 'get_event_loop')
    mocker.patch.object(app, 'supervisor')
    app.main()
    logging.getLogger.assert_called_once()
    asyncio.get_event_loop.assert_called_once()
    app.supervisor.assert_called_once()
