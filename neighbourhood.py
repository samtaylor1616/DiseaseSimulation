# neighbourhood.py - defines two different ways a neighbourhood
#                    can be updated. Go to Lecture 5 for more information
import numpy as np
# Von Neumann neighbourhood:
    # Site is the set of cells directly North, South, East, West
def vonNeumann(neighbourhood, row, col, NUM_ROWS, NUM_COLS):
    neighbours = [neighbourhood[row, col]] # main site
    if (row + 1) < (NUM_ROWS - 1):
        neighbours.append(neighbourhood[row+1, col]) # bottom
    if (row - 1) > 0:
        neighbours.append(neighbourhood[row-1, col]) # top
    if (col + 1) < (NUM_COLS - 1):
        neighbours.append(neighbourhood[row, col+1]) # right
    if (col - 1) > 0:
        neighbours.append(neighbourhood[row, col-1]) # left

    return np.array(neighbours)

# Moore neighbourhood:
    # Site is the set of cells same as Von Neumann
    # along with NE, NW, SE, SW
    # Could have used slicing however we needed to check the boarders 
    # which required if statements already
def moore(neighbourhood, row, col, NUM_ROWS, NUM_COLS):
    neighbours = []
    if (row - 1) > 0 and (col - 1) > 0:
        neighbours.append(neighbourhood[row-1, col-1]) # Top left
    if (row + 1) < (NUM_ROWS - 1) and (col - 1) > 0:
        neighbours.append(neighbourhood[row+1, col-1]) # Bottom left
    if (row - 1) > 0 and (col + 1) < (NUM_COLS - 1):
        neighbours.append(neighbourhood[row-1, col+1]) # Top right
    if (row + 1) < (NUM_ROWS - 1) and (col + 1) < (NUM_COLS - 1):
        neighbours.append(neighbourhood[row+1, col+1]) # Bottom right

    # Adds Von Neumann N,E,S,W    
    neighbours.extend(vonNeumann(neighbourhood, row, col, NUM_ROWS, NUM_COLS))
    return( np.array(neighbours) )
