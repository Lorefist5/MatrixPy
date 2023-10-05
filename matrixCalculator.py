import Functions.generic as generic
import Functions.matrixes as matrix
import Functions.userInputs as inputs
choices = {
    "add":"Addition of matrixes",
    "sub":"Substraction of matrixes"
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
    print(f"The first matrix: \n{matrix.toString(firstMatrix)}The second matrix:\n{matrix.toString(secondMatrix)}The result of the addition is: \n{matrix.toString(results)}")
if userChoice == "sub":
    #The user only enters the rows and columns once because they will be the same dimension for substraction
    rows =         inputs.getSecuredInt("Enter the amount of rows you want for both your matrixes: ")
    columns =      inputs.getSecuredInt("Enter the amount of columns you want for both your matrixes: ")

    firstMatrix =  inputs.createMatrix(rows,columns)
    secondMatrix = inputs.createMatrix(rows,columns)

    results = matrix.addMatrix(firstMatrix,secondMatrix)
    generic.clear()
    print(f"The first matrix: \n{matrix.toString(firstMatrix)}The second matrix:\n{matrix.toString(secondMatrix)}The result of the substraction is: \n{matrix.toString(results)}")


