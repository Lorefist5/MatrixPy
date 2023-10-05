import Functions.generic as generic
import Functions.matrixes as matrix
import Functions.userInputs as inputs
choices = {
    "add":"Addition of matrixes",
    "sub":"Substraction of matrixes",
    "ms":"Multiplication by scalar"
    }




userChoice = inputs.multipleChoice("Choose which calculation do you want to do.", choices,True)

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

    results = matrix.addMatrix(firstMatrix,secondMatrix)
    generic.clear()
    print(f"The first matrix:{matrix.toString(firstMatrix)}The second matrix:{matrix.toString(secondMatrix)}The result of the substraction is:{matrix.toString(results)}")
elif userChoice == "ms":
    rows =         inputs.getSecuredInt("Enter the amount of rows you want for your matrix: ")
    columns =      inputs.getSecuredInt("Enter the amount of columns you want for your matrix: ")

    myMatrix = inputs.createMatrix(rows,columns)
    scalarNumber = inputs.getSecuredInt("Enter the scalar you want to use for multiplcation: ")
    results = matrix.multiplicationByScalar(scalarNumber,myMatrix)
    print(f"The results are:{matrix.toString(results)}")

    