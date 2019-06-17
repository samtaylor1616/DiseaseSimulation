# plots.py - contains functions for creating and managing plots
import datetime # Used for uniquely time stamping the saved plots
import matplotlib.pyplot as plt
import numpy as np

def makeScatter(grid, num_r, num_c):
    r_values = []
    c_values = []
    count_values = []
    for row in range(num_r):
        for col in range(num_c):
            if grid[row,col] > 0:
                r_values.append(row)
                c_values.append(col)
                count_values.append(grid[row,col]*100)

    return(r_values, c_values, count_values)

def plotGrids(world, infected, uninfected, dead, numRows, numCols, dirPath, SHOW):
    # Gets current date and time to create a unique name
    currentDT = datetime.datetime.now()
    imageName = dirPath + str(currentDT) + ".png"

    # Infected Scatter
    Irows, Icols, Icount = makeScatter(infected, numRows, numCols)
    plt.scatter(Icols, Irows, s=Icount, c="r", alpha=0.5)

    # Uninfected Scatter
    Urows, Ucols, Ucount = makeScatter(uninfected, numRows, numCols)
    plt.scatter( Ucols, Urows, s=Ucount, c="b", alpha=0.5)

    # Killed Scatter
    Drows, Dcols, Dcount = makeScatter(dead, numRows, numCols)
    plt.scatter( Dcols, Drows, s=Dcount, c="black", alpha=0.5, marker='X')

    # World Boarder Scatter
    Wrows, Wcols, Wcount = makeScatter(world, numRows, numCols)
    plt.scatter(Wcols, Wrows, s=Wcount, c="black", alpha=1)

    plt.savefig(imageName)
    if SHOW:
        plt.show()
    else:
        plt.clf() # Resets plots

def plotCount(infCount, antiCount, deathCount, dirPath, SHOW):
    # Gets current date and time to create a unique name
    currentDT = datetime.datetime.now()
    imageName = dirPath + str(currentDT) + ".png"

    label = ["Infections", "Antidotes", "Killed"]
    index = np.arange(len(label))
    plt.title("Count of Events")
    barlist = plt.bar(index, [infCount, antiCount, deathCount])
    plt.ylabel("Number of occurrence")
    plt.xticks(index, label, rotation=20)

    # Modifying the colors
    barlist[0].set_color('r') # infect
    barlist[1].set_color('g') # antidote
    barlist[2].set_color('y') # killed

    plt.savefig(imageName)
    if SHOW:
        plt.show()
    else:
        plt.clf() # Resets plots
