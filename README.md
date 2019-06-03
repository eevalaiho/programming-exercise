# Programming exercise

## The task

Using python implement a simple web scraper, see [complete task description](documentation/cand_prog_task.md).

## Implementation

### Web-scraping

The web scraping part of the task is implemented using [```aiohttp```](https://github.com/aio-libs/aiohttp). ```Aiohttp``` is a python library that supports asynchronous web requests and concurrent execution. 

The ```app.py``` file contains the logic for supervising the asynchronous and concurrent execution of the web scraping tasks. The tasks are described simply as tuples of a regular expression and a group of url's. To demonstrate concurrent execution the scraping tasks are executed in multiple threads. For simplicity each group of urls is processed in it's own thread. In a real application a more versatile implementation would of course be needed. 

Actual web scraping code is implemented in ```scraper.py``` -file where the ```pull_urls``` method contains the main logic. There for each url the web content is first fetched and then parsed using python's ```re``` library and the regular expression provided as parameter. Finally the results are saved to a local database. To space out the requests (and not to overwhelm any servers or connections) the thread is put to sleep for a time interval (3 sec by default) after sending each request. 

The ```scrapeItem.py``` file contains the model for the scraped item. 

The ```db.py``` file contains logic for inserting scraping results in the database.

### Data storage

Scraped data is stored in a local [```SQLite```](https://www.sqlite.org/index.html) database. ```SQLite``` was chosen because of it's light-weightedness and ease of implementation. ```SQLite``` does not support concurrent writes, but the implementation can be easily migrated to use a full-fledged database engine such as ```PostgreSQL```.

The task description didn't set any specific requirements for storage format. Thus the scraped and extracted data (a list of strings) is stored in the database as one text string (along with some more information). 

## Testing 

[Testing document](documentation/testing.md)

## Installation

[Installation guide](documentation/installation.md)

## User guide

Follow the [installation guide](documentation/installation.md) to install the program. 

### Running the program

Cd to the program's main directory:

    $ cd <path-to-download-directory>/programming-exercise

Execute the program:

    $ python3 app.py

You may stop program execution at any time by typing Ctrl+C.

### Running tests

Cd to the program's main directory:

    $ cd <path-to-download-directory>/programming-exercise
    
Execute tests:

    $ pytest

