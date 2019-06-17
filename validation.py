# validation.py - contains validation functions for input

def valCommandLine(initPop, initInfected, cols, rows, numSteps):
    try:
        validateGreater(-1, initPop)
        validateGreater(-1, initInfected)
        validateGreater(1, cols)
        validateGreater(1, rows)
        validateGreater(-1, numSteps)
    except ValueError as err:
        raise ValueError(err)
    return True

def validateGreater(min, x):
    if(x < min):
        errStr = str(x) + " must be greater than " + str(min) + "\n"
        raise ValueError(errStr)
    return True

def validateProb(prob):
    if(prob < 0):
        raise ValueError("Probability must be 0 or greater not: %d" %prob)
    return True

def validateHood(hoodChoice):
    if( (hoodChoice != 'V') and (hoodChoice != 'M') ):
        raise ValueError("NEIGHBOURHOOD CHOICE must be 'V' or 'M' not: %s"%hoodChoice)
    return True

def validateYTrue(option):
    if( (option != 'Y') and (option != 'N') ):
        raise ValueError("Option choice must be 'Y' or 'N' not: %s"%option)
    return option == 'Y' # Returns True is choice is Y
