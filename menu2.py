import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def matrixSumOrDifference(matrix1,matrix2,isSubstraction):
    newMatrix = []
    
    for row in range(len(matrix1)):
        newMatrix.append([])
        for column in range(len(matrix1[row])):
            if(isSubstraction == True):
                newMatrix[row].append(matrix1[row][column] - matrix2[row][column])
            else:
                newMatrix[row].append(matrix1[row][column] + matrix2[row][column])

    return newMatrix
def multiplyByScalar(number, matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] = matrix[row][column] * number 
def multiplyByMatrix(matrix1, matrix2):
    newMatrix = []

    numRows = len(matrix1)
    numCols = len(matrix2[0])
    commonDim = len(matrix1[0])
    
    newMatrix = [[0] * numCols for _ in range(numRows)]

    for row in range(numRows):
        for column in range(numCols):
            for commonColumn in range(commonDim):
                newMatrix[row][column] += matrix1[row][commonColumn] * matrix2[commonColumn][column]

    return newMatrix

def createMatrix():
    newMatrix = []
    
    rows = int(input("How many rows do you want to have?: "))
    columns = int(input("How many columns do you want to have?: "))
    clear()
    #Defines the rows
    for row in range(rows):
        newMatrix.append([])

    #Defines the columns
    for row in range(len(newMatrix)):
        for column in range(columns):
            newMatrix[row].append(0)
    #Asks the user to enter values
    for row in range(len(newMatrix)):
        for column in range(columns):
            userInput = int(input("Enter the value you want for your matrix?: "))
            newMatrix[row][column] = userInput
            print(newMatrix)
    clear()
    return newMatrix
def multipleChoice(promt,answers, errorHandler = "Try again", toLower = True):
    inputIsAnswer = False
    userInput = ""
    while inputIsAnswer != True:
        if toLower:
            userInput = input(promt).lower()
        else:
            userInput = input(promt)
        for answer in answers:
            if userInput == str(answer):
                inputIsAnswer = True
        if inputIsAnswer != True:
            os.system('cls' if os.name == 'nt' else 'clear') # clears the console everytime theres an error
            print(errorHandler)
    return userInput


def handleSumOrDifference(subtract):
    matrix1 = createMatrix()
    matrix2 = createMatrix()
    results = matrixSumOrDifference(matrix1,matrix2, subtract)
    clear()
    return results
def handleMultiplyByScalar():
    userInput = int(input("Enter the scalar you want you use: "))
    matrix1 = createMatrix()
    multiplyByScalar(userInput,matrix1)
    clear()
    return matrix1
  
typeOfOperation = multipleChoice("What type of operation do you want to do? \naddition(sum)\nsubtraction(sub)\nmult by scalar(ms)\nmult by matrix(mm)?\n",
                               ["sum","sub","ms","mm"])#All the posible answers


if typeOfOperation == "sum":
    print(handleSumOrDifference(False))
elif typeOfOperation == "sub":
    print(handleSumOrDifference(True))
elif typeOfOperation == "ms":
    print(handleMultiplyByScalar())
elif typeOfOperation == "mm":
    matrix1 = createMatrix()
    matrix2 = createMatrix()
    results = multiplyByMatrix(matrix1, matrix2)
    print(results)
