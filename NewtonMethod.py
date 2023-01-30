#################################################################
# Author:   Clay Fulk
# Date:     January 24, 2023
# Brief:    Uses Newton's Method to find a root of a function, 
#           given an initial guess. The input required includes 
#           a function, its derivative, and an initial guess.
#################################################################


import math         # For function input


# Brief:            Evaluates initial function
# xVal:             x-value to substitute for each 'x' in function
def func(xVal):
    newFuncString = funcString.replace("x", str(xVal))     # Substitute all x's in function
    return eval(newFuncString)     # Evaluate function and return result


# Brief:            Evaluates initial function's derivative
# xVal:             x-value to substitute for each 'x' in function
def der(xVal):
    newDerString = derString.replace("x", str(xVal))       # Substitute all x's in function
    return eval(newDerString)      # Evaluate function and return result


# Brief:            Finds a root of a funtion using Newton's Method
# lastGuess:        Last guess computed (x_n-1)
# iterationCounter: Number of iterations performed (Defaults to 0)
def newtonMethod(lastGuess, iterationCounter=0):

    # Base Case: reached iteration limit
    if (iterationCounter >= iterationLimit):
        print("Method did not converge in time. Stopped after", str(iterationCounter), "iterations.")
        return lastGuess

    # Iteration formula
    nextGuess = lastGuess - (func(lastGuess))/(der(lastGuess))

    # Convergence Test
    if (abs(nextGuess - lastGuess) < marginOfError):
        print("Method converged after", str(iterationCounter), "iterations.")
        return nextGuess

    # Recursive Case
    return newtonMethod(nextGuess, iterationCounter + 1)


# Main Program
if __name__ == "__main__":
    
    iterationLimit = 50     # Number of iterations allowed
    marginOfError = 0.0001  # 10^-5
    funcString = input("Input function (formatting ex.: math.cos(x) + 3*x**2 + 1): ")   # Get initial function
    derString = input("Input function's derivative (same formatting as function): ")    # Get initial function's derivative

    # Get initial guess
    initialGuess = ""
    while (type(initialGuess) != float):
        try:
            initialGuess = float(eval(input("Input initial guess (math symbols can be used. Ex.: math.cos(), math.pi): ")))
        except:
            print("Invalid input given. Use only math expressions and symbols.")

    print("Finding a root...")

    # Compute root
    try:
        print("Root: x =", str(newtonMethod(initialGuess)))
    except:
        print("Error encountered. Invalid input was likely given.")