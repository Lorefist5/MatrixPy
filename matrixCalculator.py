import Functions.generic as generic
import Functions.matrixes as matrix
import Functions.userInputs as inputs


#These are the calculations the user can choose
choices = {
    "add":"Addition of matrixes",
    "sub":"Substraction of matrixes",
    "ms":"Multiplication by scalar",
    "mm":"Multiplication by matrix",
    "dt":"Get the determinant of a matrix",
    "mn": "Get the minors of the matrix",
    "cf":"Get the cofactors of the matrix",
    "inv":"Get the inverse of the matrix"
    }


userChoice = inputs.multipleChoice("Choose which calculation do you want to do.", choices,True) #We set the last parameter to true so that it prints the options to the console (optional)

if userChoice == "add":
    #The user only enters the rows and columns once because they will be the same dimension for addition
    rows =         inputs.getSecuredInt("Enter the amount of rows you want for both your matrixes: ")
    columns =      inputs.getSecuredInt("Enter the amount of columns you want for both your matrixes: ")

    firstMatrix =  inputs.createMatrix(rows,columns)
    secondMatrix = inputs.createMatrix(rows,columns)

    results = matrix.addMatrix(firstMatrix,secondMatrix)
    generic.clear()
    print(f"The first matrix:{matrix.toString(firstMatrix)}The second matrix:{matrix.toString(secondMatrix)}The result of the addition is:{matrix.toString(results)}")

elif userChoice == "sub":
    #The user only enters the rows and columns once because they will be the same dimension for substraction
    rows =         inputs.getSecuredInt("Enter the amount of rows you want for both your matrixes: ")
    columns =      inputs.getSecuredInt("Enter the amount of columns you want for both your matrixes: ")

    firstMatrix =  inputs.createMatrix(rows,columns)
    secondMatrix = inputs.createMatrix(rows,columns)

    results = matrix.subtractMatrix(firstMatrix,secondMatrix)
    generic.clear()
    print(f"The first matrix:{matrix.toString(firstMatrix)}The second matrix:{matrix.toString(secondMatrix)}The result of the substraction is:{matrix.toString(results)}")

elif userChoice == "ms":
    rows =         inputs.getSecuredInt("Enter the amount of rows you want for your matrix: ")
    columns =      inputs.getSecuredInt("Enter the amount of columns you want for your matrix: ")

    myMatrix =     inputs.createMatrix(rows,columns)
    scalarNumber = inputs.getSecuredInt("Enter the scalar you want to use for multiplcation: ")
    results =      matrix.multiplicationByScalar(scalarNumber,myMatrix)
    print(f"The results are:{matrix.toString(results)}")

elif userChoice == "mm":
    firstMatrixRows =     inputs.getSecuredInt("Enter the rows you want for your first matrix: ")
    #This will define the columns for the first matrix and the rows for the second matrix
    matrix1CMatrix2R =    inputs.getSecuredInt("Enter the columns you want for your first matrix and the rows you want for your second column: ")
    secondMatrixColumns = inputs.getSecuredInt("Enter the columns you want for your second matrix: ")

    firstMatrix =  inputs.createMatrix(firstMatrixRows,matrix1CMatrix2R)
    secondMatrix = inputs.createMatrix(matrix1CMatrix2R, secondMatrixColumns)

    results = matrix.multiplyByMatrix(firstMatrix,secondMatrix)
    print(f"The first matrix:{matrix.toString(firstMatrix)}The second matrix:{matrix.toString(secondMatrix)}The result of the multiplication is:{matrix.toString(results)}")
elif userChoice == "dt":
    fixedSizes = {
        "2":"2x2",
        "3":"3x3"
    }
    
    size =        int(inputs.multipleChoice("Enter the size of your matrix.",fixedSizes,True))
    myMatrix =    inputs.createMatrix(size,size)
    determinant = matrix.getDeterminant(myMatrix)
    print(f"The determinant of this matrix is {determinant}")
elif userChoice == "mn":
    fixedSizes = {
        "2":"2x2",
        "3":"3x3"
    }

    size =     int(inputs.multipleChoice("Enter the size of your matrix.",fixedSizes,True))
    myMatrix = inputs.createMatrix(size,size)
    if matrix.getDeterminant(myMatrix) == 0:
        print("The matrix is singular (determinant is zero).")
    else:
        minors = matrix.minorsOfMatrix(myMatrix)
        print(f"The minors of this matrix are {matrix.toString(minors)}")
elif userChoice == "cf":
    fixedSizes = {
        "2":"2x2",
        "3":"3x3"
    }

    size = int(inputs.multipleChoice("Enter the size of your matrix.",fixedSizes,True))
    myMatrix = inputs.createMatrix(size,size)
    if matrix.getDeterminant(myMatrix) == 0:
        print("The matrix is singular (determinant is zero).")
    else:
        minors = matrix.cofactorsOfMatrix(myMatrix)
        print(f"The minors of this matrix are {matrix.toString(minors)}")
elif userChoice == "inv":
    fixedSizes = {
        "2":"2x2",
        "3":"3x3"
    }

    size =     int(inputs.multipleChoice("Enter the size of your matrix.",fixedSizes,True))
    myMatrix = inputs.createMatrix(size,size)
    if matrix.getDeterminant(myMatrix) == 0:
        print("The matrix is singular (determinant is zero).")
    else:
        minors = matrix.inverseMatrix(myMatrix)
        print(f"The minors of this matrix are {matrix.toString(minors)}")