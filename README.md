# Programming exercise

## Task

A python programming exercise to implement a simple web scraper, see [complete task description](documentation/cand_prog_task.md).

## Implementation

The web scraping part of the task is implemented using python's asyncio library that supports asynchronous web requests and concurrent execution. For simplicity each url_group is processed in it's own thread. In a real application a more versatile implementation would of course be needed. After sending each request the thread is put to sleep for a certain interval (1 sec by default). This is to not to flood connections. 

Scraped data is stored in a local SQLite database. SQLite was chosen because of it's light-weightedness and ease of implementation. SQLite does not support concurrent writes, but the implementation can be easily trasformed so that it supports a full database engine, for example PostgreSQL.

The scraped data is stored as it is since the task description didn't set any requirements for that. 


## Installation

[Installation guide](documentation(installation.md)

## User guide





