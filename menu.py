import os
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

def inputMatrix():
    arrays = []
    currentMatrix = []
    currentArray = []

    while True:
        userInput = input("Enter a number, 'next array', 'next matrix', 'end', or 'd' to delete the last item: ").strip().lower()

        if userInput == 'end':
            if currentArray:
                currentMatrix.append(currentArray)
            if currentMatrix:
                arrays.append(currentMatrix)
            break
        elif userInput == 'next array' or userInput == "na":
            if currentArray:
                currentMatrix.append(currentArray)
            currentArray = []
        elif userInput == 'next matrix' or userInput == "nm":
            if currentArray:
                currentMatrix.append(currentArray)
                currentArray = []
            if currentMatrix:
                arrays.append(currentMatrix)
            currentMatrix = []
        elif userInput == 'd':
            if currentArray:
                itemRemoved = currentArray.pop()  # Delete the last item in the current array
                print(f"You removed {itemRemoved}")
            else:
                print("Current array is empty. Nothing to delete.")
        else:
            try:
                number = float(userInput)
                currentArray.append(number)
            except ValueError:
                print("Invalid input. Enter a number or one of the commands.")

    return arrays


def securedInt(promt,errorHandler = "Invalid input."):
    error = True
    while error:
        try:
            results = int(input(promt))
            error = False
        except ValueError:
            print(errorHandler)
    return results
def inputArray():
    newArray = []
    userInput = ""
    while userInput != "end":
        userInput = input("Enter a number, or 'end': ")
        if userInput != "end":
            try:
                number = float(userInput)
                newArray.append(number)
            except ValueError:
                print("Invalid input. Enter a number or one of the commands.")
    return newArray


def multArrayByScalar():
    scalarNumber = securedInt("Enter a scalar number: ")
    array = inputArray()
    newArray = [number * scalarNumber for number in array]
    return newArray

def addMatrix(arrays):
    resultMatrix = [[0] * len(arrays[0][0]) for _ in range(len(arrays[0]))]

    for matrix in arrays:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                resultMatrix[i][j] += matrix[i][j]

    return resultMatrix
def subMatrix(arrays):
    resultMatrix = [[0] * len(arrays[0][0]) for _ in range(len(arrays[0]))]

    for matrix in arrays:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                resultMatrix[i][j] -= matrix[i][j]

    return resultMatrix
def multiplyMatrix(matrices):
    if not isinstance(matrices, list) or len(matrices) != 2:
        return "Input must be a list of two matrices."

    matrix1, matrix2 = matrices

    if len(matrix1[0]) != len(matrix2):
        return "Number of columns in the first matrix must match the number of rows in the second matrix for multiplication."

    num_rows = len(matrix1)
    num_cols = len(matrix2[0])
    common_dim = len(matrix1[0])

    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(common_dim):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

typeOfNumbers = multipleChoice("What type of operation do you want to do? \naddition(sum)\nsubtraction(sub)\nmult by scalar(ms)\nmult by matrix(mm)?\n",
                               ["sum","sub","ms","mm"])#All the posible answers

if typeOfNumbers == "sum":
        arrays = inputMatrix()
        print(addMatrix(arrays))
elif typeOfNumbers == "sub":
    arrays = inputMatrix()
    print(subMatrix(arrays))
elif typeOfNumbers == "ms":
        print(f"Results: {multArrayByScalar()}")
elif typeOfNumbers == "mm":
    arrays = inputMatrix()
    print(multiplyMatrix(arrays))