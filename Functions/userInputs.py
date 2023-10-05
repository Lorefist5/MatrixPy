from .generic import clear

def getSecuredInt(promt = "Enter the integer: ", errorHandler = "The input must be an integer"):
    noError = False
    userInput = 0
    while(not noError):
        try:
            userInput = int(input(promt))
            noError = True
        except:
            clear()
            print(errorHandler)
            noError = False
    return userInput
def multipleChoice(choices):
    #choices will be a dictionary
    print("")


def createMatrix():
    rows = getSecuredInt("How many rows do you want to have in your matrix?: ")
    columns = getSecuredInt("How many columns do you want to have in your matrix?: ")
    #This code will add empty arrays that will represent the rows
    myMatrix = [[] for row in range(rows)]
    #This code will make all the columns = 0 by default
    for row in range(len(myMatrix)):
        for column in range(columns):
            myMatrix[row].append(0)
    currentColumn = 0
    currentRow = 0
    
    while(currentRow < rows):
        userInput = getSecuredInt(f"Enter the value [{currentRow}][{currentColumn}]: ")
        myMatrix[currentRow][currentColumn] = userInput
        print(f"Your current matrix is {myMatrix}")
        currentColumn += 1
        if currentColumn >= columns:
            currentRow+= 1
            currentColumn = 0
        

    return myMatrix
    