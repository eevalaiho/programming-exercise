# Programming exercise

## Task

A python programming exercise to implement a simple web scraper, see [complete task description](documentation/cand_prog_task.md).

## Implementation

### Web-scraping

The web scraping part of the task is implemented using [aiohttp](https://github.com/aio-libs/aiohttp) which is a python library that supports asynchronous web requests and concurrent execution. 

For simplicity each url_group is processed in it's own thread. In a real application a more versatile implementation would of course be needed. To space out the requests (and to not overwhelm servers) the thread is put to sleep for a certain time interval (3 sec by default) after sending each request. 

### Data storage

Scraped data is stored in a local [SQLite](https://www.sqlite.org/index.html) database. SQLite was chosen because of it's light-weightedness and ease of implementation. SQLite does not support concurrent writes, but the implementation can be easily trasformed so that it supports a full database engine, for example PostgreSQL.

The task description didn't set any specific requirements for storage format. The scraped and extracted data is stored as a json string. Json format was chosen mainly because python supports json natively and json is easily queryable. 

## Installation

[Installation guide](documentation/installation.md)

## User guide

First cd to the program's main directory:

    $ cd <download-dorectory>/CGI-programming-exercise

To run the program command:

    $ python3 src/main.py

You can stop program execution any time by typing Ctrl+C.





