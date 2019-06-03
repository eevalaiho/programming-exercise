# Installation

1. Cd to the directory where you want to clone the repository:

        $ cd <path-to-the-directory>
1. Clone the repository:

        $ git clone https://github.com/eevalaiho/programming-exercise.git
1. Cd to program's main directory:

        $ cd programming-exercise
1. Create an ```Anaconda``` environment for the application:

        $ conda create -n <env-name> python=3.6 aiohttp pytest pytest-asyncio pytest-mock
1. Activate the environment

        $ source activate <env-name>     
1. Install libraries

    [```pytest-mock```](https://anaconda.org/conda-forge/pytest-mock)
    $ conda install -c conda-forge pytest-mock
1. Initialize database

        $ python3 init_app.py
        
To run the program command:

    $ python3 scraper
You can stop program execution by typing Ctrl+C.
