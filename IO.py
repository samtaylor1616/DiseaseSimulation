# IO.py - input and output

import datetime # Used for uniquely creating a directory
import os       # Used to check if directory exists

def setUpEnvironment():
    my_path = os.getcwd()               # Gets current working directory
    currentDT = datetime.datetime.now() # Gets current date and time 
    dirPath = my_path + '/Plots/Disease ' + str(currentDT) + '/'
    if not os.path.isdir('./Plots/'):
        os.mkdir('./Plots/')
    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)

    return dirPath
