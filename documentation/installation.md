# Installation guide

## Program installation

1. Cd to the directory where you want to clone the repository:

        $ cd <path-to-the-directory>
1. Clone the repository:

        $ git clone https://github.com/eevalaiho/programming-exercise.git
1. Cd to program's main directory:

        $ cd programming-exercise
1. Create an [```Anaconda```](https://anaconda.org/) environment for the application:

        $ conda create -n <env-name> python=3.6
1. Activate the environment

        $ source activate <env-name>     
1. Install libraries [```aiohttp```](https://anaconda.org/conda-forge/aiohttp)
    
        $ conda install -c conda-forge aiohttp

1. Initialize application

    Running the init_app.py command will create a local database file in subdirectory ```data``` and append project path in python path.

        $ python3 init_app.py
To run the program command:

    $ python3 app
    
You can stop program execution by typing Ctrl+C.



## **Optional** installation for testing

1. Install libraries [```pytest```](https://anaconda.org/conda-forge/pytest), [```pytest-mock```](https://anaconda.org/conda-forge/pytest-mock), [```pytest-mock```](https://anaconda.org/conda-forge/pytest-async)
    
        $ conda install -c conda-forge pytest pytest-mock pytest-async

To run tests command:

    $ pytest

