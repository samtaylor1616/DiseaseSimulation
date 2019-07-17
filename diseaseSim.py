#
# diseaseSim.py - simulates the spread of disease through a population
#
# Usage: 
#   1. python3 diseaseSim.py
#   2. python3 diseaseSim.py <'V'/'M'> < POPULATION > < INFECTED > < COLS > < ROWS > 
#                                 < STEPS > <'Y'/'N'> [< infect prob > < heal prob >]

import sys
import numpy as np

from IO import *
from plots import *
from validation import *
from worldOps import *

def printUsage():
    print("\nUsage: python3 " + sys.argv[0] + "<'V'/'M'> < POPULATION >", end='')
    print("< INFECTED > < COLS > < ROWS > < STEPS > <'Y'/'N'> [< infect prob > < heal prob >]")
    print("\t'V' for Von Neumann neighbourhood")
    print("\t'M' for Moore neighbourhood")
    print("\t'Y' to display plots automatically")
    print("\t'N' to NOT display plots")
    print("\nChange probability of infection and healing via: < infect prob > < heal prob >")

def printProbs():
    print("\tDEATH PROBABILITY:", DIE_PROB)
    print("\tINFECTION PROBABILITY:", INFECT_PROB)
    print("\tHEALING PROBABILITY:", HEAL_PROB, "\n")

def printParams():
    print("\tHOOD CHOICE:", HOOD_CHOICE)
    print("\tINIT POPULATION:", INIT_POP)
    print("\tINIT INFECTED:", INIT_INFECTED)
    print("\tNUMBER OF ROWS:", NUM_ROWS)
    print("\tNUMBER OF COLS:", NUM_COLS)
    print("\tNUMBER OF STEPS:", NUM_STEPS, "\n")
    printProbs()

def printStats():
    print()
    print(infected.sum(), " out of ", TOTAL_POP, "cells are INFECTED")
    print(uninfected.sum(), " out of ", TOTAL_POP, "cells are UNINFECTED")
    print(dead.sum(), " out of ", TOTAL_POP, "cells are DEAD")

# Default Rows: 15
# Default Cols: 15
# Default steps: 10
def setRowColStep():
    return (15,15,10)

# Default Probability
# Default die: 0.10
# Default infect: 0.90
# Default heal: 0.07
def setProb():
    return(0.10, 0.90, 0.07)

# ****************************** PROGRAM BEGINS HERE ******************************
HOOD_CHOICE = 'V'
SHOW = True
INIT_POP = 100
INIT_INFECTED = 5

NUM_ROWS, NUM_COLS, NUM_STEPS = setRowColStep()
DIE_PROB, INFECT_PROB, HEAL_PROB = setProb()

# TOTAL COUNTERS
dead_count = 0
infect_count = 0
antidote_count = 0

# To produce reproducible data
random.seed(1)
# Sets up a folder in the directory to save plots into
dirPath = setUpEnvironment() 
valid = True

argLen = len(sys.argv)
if (argLen != 8) and (argLen != 10):
    printUsage()
    print("\nUsing default values...")
else:
    try: 
        # Setting Command Line Arguments
        HOOD_CHOICE = sys.argv[1][0].upper()
        INIT_POP = int(sys.argv[2])
        INIT_INFECTED = int(sys.argv[3])
        NUM_COLS = int(sys.argv[4])
        NUM_ROWS = int(sys.argv[5])
        NUM_STEPS = int(sys.argv[6])
        SHOW = validateYTrue(sys.argv[7][0].upper())

        # Input Validation
        valCommandLine(INIT_POP, INIT_INFECTED, NUM_COLS, NUM_ROWS, NUM_STEPS)
        validateHood(HOOD_CHOICE)
        print("\nUsing command line arguments:")
        if(argLen == 10):
            INFECT_PROB = float(sys.argv[8])
            HEAL_PROB = float(sys.argv[9])
            validateProb(INFECT_PROB)
            validateProb(HEAL_PROB)
    except TypeError as err:
        print("\nParameter %s entered is not a number\n" % err)
        valid = False
    except ValueError as err:
        print("\nERROR: Command line argument: %s\n" %err)
        valid = False

if valid:
    TOTAL_POP = INIT_POP + INIT_INFECTED
    printParams()

    # Sets neighbourhood function
    if HOOD_CHOICE == 'M':
        NEIGH_FUNC = moore
    else: # HOOD_CHOICE == 'V'
        NEIGH_FUNC = vonNeumann

    # Initialising world
    world = np.zeros((NUM_ROWS, NUM_COLS), dtype=np.int)
    initialiseBoarders(world, NUM_ROWS, NUM_COLS)

    # Initialising cells
    infected = np.zeros((NUM_ROWS, NUM_COLS), dtype=np.int)
    uninfected = np.zeros((NUM_ROWS, NUM_COLS), dtype=np.int)
    dead = np.zeros((NUM_ROWS, NUM_COLS), dtype=np.int)

    distribute(world, infected, NUM_ROWS, NUM_COLS, INIT_INFECTED)
    distribute(world, uninfected, NUM_ROWS, NUM_COLS, INIT_POP)

    plotGrids(world, infected, uninfected, dead, NUM_ROWS, NUM_COLS, dirPath, SHOW)

    # ****************************** START SIMULATION ******************************
    for timestep in range(NUM_STEPS):
        print("\n###################### TIMESTEP", timestep, "#####################\n")
        infected2 = np.zeros((NUM_ROWS, NUM_COLS), dtype=np.int)
        uninfected2 = np.zeros((NUM_ROWS, NUM_COLS), dtype=np.int)
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                dead_count += modify(NEIGH_FUNC, NUM_ROWS, NUM_COLS, infected, dead, row, col, DIE_PROB, "##### New dead cell")
                infect_count += modify(NEIGH_FUNC, NUM_ROWS, NUM_COLS, infected, uninfected, row, col, INFECT_PROB, "***** New infection")
                antidote_count += modify(NEIGH_FUNC, NUM_ROWS, NUM_COLS, infected, uninfected, row, col, HEAL_PROB, "~~~~~ New antidote")

                movePeeps(NUM_ROWS, NUM_COLS, world, infected, infected2, row, col)
                movePeeps(NUM_ROWS, NUM_COLS, world, uninfected, uninfected2, row, col)
        infected = infected2
        uninfected = uninfected2
        printStats()
        plotGrids(world, infected, uninfected, dead, NUM_ROWS, NUM_COLS, dirPath, SHOW)

    print("\n###################### Final Results #####################\n")

    print("\nTotal number of infections that occurred: ", infect_count)
    print("Total number of antidotes given: ", antidote_count)
    print("Total number of cells killed: ", dead_count)

    plotCount(infect_count, antidote_count, dead_count, dirPath, SHOW)

print("\n########################## Done ##########################\n")
