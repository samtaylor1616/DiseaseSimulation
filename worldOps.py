# worldOps.py - Contains functions of operations to be implemented on the world
import random
from neighbourhood import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ START INITIALISATION FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~  #

def initialiseBoarders(world, r, c):
    # Create box around world
    world[:1, :] = 1
    world[r-1: , :] = 1
    world[:,0:1] = 1
    world[:, c-1: ] = 1
    
    # Create middle boarder
    halfR = int(r / 2)
    halfC = int(c / 2)
    world[halfR:halfR+1, :] = 1
    world[:, halfC:halfC +1] = 1
    
    # Make doors
    world[halfR, halfC-1] = 0
    world[halfR-1, halfC] = 0

def distribute(world, grid, num_r, num_c, numpeep):
    for i in range(numpeep):
        rpos = random.randint(0, num_r-1)
        cpos = random.randint(0, num_c-1)
        while(world[rpos, cpos] == 1):
            rpos = random.randint(0, num_r-1)
            cpos = random.randint(0, num_c-1)
        grid[rpos, cpos] += 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ END INITIALISATION FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~  #

def movePeeps(NUM_ROWS, NUM_COLS, world, cur, next, r, c):
    for peep in range(cur[r,c]):
        rMove = random.randint(-1,1)
        cMove = random.randint(-1,1)

        # Out of bounds Check
        if (r + rMove) > (NUM_ROWS-1) or (r + rMove) < 0 or (1 == world[r + rMove][c]): 
            rMove = 0
        if (c + cMove) > (NUM_COLS-1) or (c + cMove) < 0 or (1 == world[r][c + cMove]):
            cMove = 0
        if (1 == world[r + rMove][c + cMove]):
            rMove = 0
            cMove = 0
        next[r + rMove, c + cMove] +=1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ START CELL FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~  #
# NOTE: NEIGH_FUNC stores either the Moore or the Von Neumann function

def modify(NEIGH_FUNC, num_rows, num_cols, inf, notinf, r, c, prob, modType):
    prob = prob * ( NEIGH_FUNC(inf, r, c, num_rows, num_cols).mean() )
    count = 0
    # If prob is not 0.0 
    if prob:
        for peep in range(inf[r,c]):
            if random.random() < prob:
                inf[r, c] -=1
                notinf[r, c] +=1
                print( modType, " (", r, ",", c, ")")
                count += 1
    return count

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ END CELL FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~  #