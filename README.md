## Usage - diseaseSim.py:
   1. Default values: python3 diseaseSim.py
   2. python3 diseaseSim.py <'V'/'M'> < POPULATION > < INFECTED > < COLS > < ROWS > 
                                 < STEPS > <'Y'/'N'> [< infect prob > < heal prob >]

    Example to copy: $ python3 diseaseSim.py V 100 60 15 15 10 Y [0.60 0.15]

## Usage - disease_sweep.sh:
    ./disease_sweep.sh <neighbourhood> <pop> <infected> <row/col step> <low_row>
                       <high_row> <low_col> <high_col>

    Example to copy: $ ./disease_sweep.sh M 100 20 10 15 25 15 25


## Contents
* diseaseSim.py       - simulates the spread of disease though a population
* disease_sweep       - bash script using the disease simulation
* neighbourhood.py    - defines Moore and vonNeumann neighbourboods
* plots.py            - contains functions for plotting and managing plots
* validation.py       - contains input validation
* worldOps.py         - contains functions of operations implemented on world
                        - ie. creating borders, moving cells, distribute
                        - along with infecting, curing, and killing cells
* disease_sweep.py    - Parameter sweep script, creates directory for experiment
                        - processes the command line arguments 
* IO.py               - Sets up output environment for saving the plots

## Dependencies

* diseaseSim.py - neighbourhood.py, plots.py, validation.py, worldOps.py, IO.py
* disease_sweep.sh - diseaseSim.py and its dependencies
