import math
from random import uniform

# Initialize state

t = [0, 0, 1, 1]
X = [
    [-0.3, 0.6],
    [0.3, -0.6],
    [1.2, -1.2],
    [1.2, 1.2]
]

# Calculation phase

def calculateWeights(X, t, min, max, funNum):
    temp = getDifferrentNumber(t[0])
    y = [temp] * len(t)    

    numOfIterations = 0
    while (y != t):
        numberOfWeights = len(X[0]) + 1
        w = getArrayOfRandomNumbers(min, max, numberOfWeights)
        for i in range(len(X)):
            calculationResult = getA(X[i], w)
            y[i] = chooseFunction(funNum, calculationResult)
        numOfIterations += 1
        if (y == t):
            print("Iterations: " + str(numOfIterations))
            print("Found correct weights: " + str(w))
            print("Class t: " + str(y))

# Step and Sigmoid functions

def stepActivationFunction(a):
    if (a >= 0):
        return 1
    else:
        return 0

def sigmoidActivationFunction(a):
    if (1 / (1 + math.exp(-a)) >= 0.5):
        return 1
    else:
        return 0

def chooseFunction(number, a):
    if (number == 0):
        return stepActivationFunction(a)
    else:
        return sigmoidActivationFunction(a)

# Helper functions

def getArrayOfRandomNumbers(min, max, length):
    arrayOfRandomNumbers = []
    for _ in range(length):
        arrayOfRandomNumbers.append(uniform(min, max))
    return arrayOfRandomNumbers

def getA(x, w):
    return w[0] + w[1] * x[0] + w[2] * x[1]

def getDifferrentNumber(number):
    if number == 0:
        return 1
    else:
        return 0

# Main function

def main():
    print("Type 0 if you want step function and 1 if you want sigmoid function:")
    chosenFunction = input()
    print("Started main...")
    print("Step function: ")
    for _ in range(5):
        calculateWeights(X, t, -3, 3, chosenFunction)

if __name__ == "__main__":
    main()