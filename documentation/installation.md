# Installation

1. Cd to the directory where you want to clone the repository:

        $ cd <path-to-the-directory>
1. Clone the repository:

        $ git clone https://github.com/eevalaiho/CGI-programming-exercise.git
1. Cd to program's main directory:

        $ cd programming-exercise
1. Create an Anaconda environment for the application:

        $ conda create -n <env-name> python=3.6 aiohttp pytest
1. Activate the environment

        $ source activate <env-name>
1. Initialize database

        $ python3 init_db.py
        
To run the program command:

    $ python3 scraper
You can stop program execution by typing Ctrl+C.
