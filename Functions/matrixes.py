def addMatrix(firstMatrix, secondMatrix):
    resultMatrix = createSameSizeMatrix(firstMatrix)
    for row in range(len(firstMatrix)):
        for column in range(len(firstMatrix[row])):
            resultMatrix[row][column] = firstMatrix[row][column] + secondMatrix[row][column]
    return resultMatrix

def subtractMatrix(firstMatrix,secondMatrix):
    resultMatrix = createSameSizeMatrix(firstMatrix)
    for row in range(len(firstMatrix)):
        for column in range(len(firstMatrix[row])):
            resultMatrix[row][column] = firstMatrix[row][column] - secondMatrix[row][column]
    return resultMatrix

def multiplyByMatrix(matrix1, matrix2):
    resultMatrix = []

    numRows = len(matrix1)
    numCols = len(matrix2[0])
    commonDim = len(matrix1[0])

    resultMatrix = [[0] * numCols for _ in range(numRows)]

    for row in range(numRows):
        for column in range(numCols):
            for commonColumn in range(commonDim):
                resultMatrix[row][column] += matrix1[row][commonColumn] * matrix2[commonColumn][column]

    return resultMatrix

def multiplicationByScalar(scalar, myMatrix):
    resultMatrix = createSameSizeMatrix(myMatrix)
    for row in range(len(myMatrix)):
        for column in range(len(myMatrix[row])):
            resultMatrix[row][column] = scalar * myMatrix[row][column]
    return resultMatrix

def getDeterminant(matrix):
    rows = getRows(matrix)
    columns = getColumns(matrix)
    
    firstPart = 0
    secondPart = 0
    if(rows == 2): #If the matrix is a 2x2 it only needs to do this
        firstPart = matrix[0][0] * matrix[1][1]
        secondPart = matrix[0][1] * matrix[1][0]
    elif(rows == 3):
        extendedMatrix = extendMatrix(matrix)
        newSize = getColumns(extendedMatrix) - 1
        for i in range(3):
            firstPart += extendedMatrix[0][i] * extendedMatrix[1][i + 1] * extendedMatrix[2][i + 2]

            secondPart += extendedMatrix[0][newSize - i] * extendedMatrix[1][newSize - (i + 1)] * extendedMatrix[2][newSize - (i + 2)]

    return firstPart - secondPart
    

def removeColumn(columnIndex,matrix):
    oldMatrixRows = getRows(matrix)
    oldMatrixColumns = getColumns(matrix)
    resultMatrix = createFixedSizeMatrix(oldMatrixRows,oldMatrixColumns - 1)
    
    for row in range(len(matrix)):
        currentColumn = 0
        for column in range(len(matrix[row])):
           if column != columnIndex:
               resultMatrix[row][currentColumn] = matrix[row][column]
               currentColumn += 1

    return resultMatrix

def removeRow(rowIndex,matrix):
    resultMatrix = []
    for row in range(len(matrix)):
        if row != rowIndex:
            resultMatrix.append(matrix[row])
    return resultMatrix

def createSameSizeMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    resultMatrix = [[] for row in range(rows)]
    for row in range(len(resultMatrix)):
        for column in range(columns):
            resultMatrix[row].append(0)
    return resultMatrix

#Getter functions
def getRows(matrix):
    rows = len(matrix)
    return rows

def getColumns(matrix):
    columns = len(matrix[0])
    return columns
#Misc functions for matrixes
def createFixedSizeMatrix(rows,columns):
    resultMatrix = [[] for row in range(rows)]
    for row in range(len(resultMatrix)):
        for column in range(columns):
            resultMatrix[row].append(0)
    return resultMatrix

def extendMatrix(matrix):
    rows =    getRows(matrix)
    columns = getColumns(matrix)
    if rows != 3 or columns != 3:
        return Exception("The matrix must be 3x3 for it to be extended.")
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
           if column == 0 or column == 1:
               matrix[row].append(matrix[row][column])
    return matrix

def toString(matrix):
    myMatrixString = "\n"

    for row in matrix:
        myMatrixString += "["
        columnIndex = 0
        for column in row:
            myMatrixString += f"{column}"
            if columnIndex < len(row) - 1:
                myMatrixString += ","
            columnIndex += 1
        myMatrixString += "]\n" 

    return myMatrixString


