def addMatrix(firstMatrix, secondMatrix):
    
    resultMatrix = createSameSizeMatrix(firstMatrix)
    for row in range(len(firstMatrix)):
        for column in range(len(firstMatrix[row])):
            resultMatrix[row][column] = firstMatrix[row][column] + secondMatrix[row][column]
    return resultMatrix


def createSameSizeMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    resultMatrix = [[] for row in range(rows)]
    for row in range(len(resultMatrix)):
        for column in range(columns):
            resultMatrix[row].append(0)
    return resultMatrix