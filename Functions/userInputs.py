from .generic import clear


#Full on user input stuff
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
def multipleChoice(prompt,choices = {}, printChoices = False):
    #choices will be a dictionary
    if printChoices:
        for choice in choices:
            prompt += f"\n({choice}){choices[choice]}"
    userInputIsChoice = False
    userInput = None
    prompt += "\n"
    while(not userInputIsChoice):
        
        userInput = input(prompt)
        for choice in choices:
            if userInput == choice:
                userInputIsChoice = True
        if not userInputIsChoice:
            clear()
            print("You need to choose one of the avaible choices.")
    return userInput
    
    

    

# Matrix related operation that requires user input
def createMatrix(rows,columns):
    """
    This function is to create matrixes via console based user inputs


    Returns:
        type: Matrix of x rows and y columns
    """
    #This code will add empty arrays that will represent the rows
    myMatrix = [[] for row in range(rows)]
    #This code will make all the columns = 0 by default
    for row in range(len(myMatrix)):
        for column in range(columns):
            myMatrix[row].append(0)
    currentColumn = 0
    currentRow = 0
    
    while(currentRow < rows):
        userInput = input(f"Enter the value [{currentRow}][{currentColumn}]: ")
        if "," in userInput:
            parsedUserInput = userInput.split(",")[:columns*rows]
            for number in parsedUserInput:
                try:
                    int(number)
                    myMatrix[currentRow][currentColumn] = int(number)
                    currentColumn += 1
                    if currentColumn >= columns:
                        currentRow+= 1
                        currentColumn = 0
                except:
                    continue
            print(f"Your current matrix is {myMatrix}")
        else:
            try:
                int(userInput)
                myMatrix[currentRow][currentColumn] = int(userInput)
                print(f"Your current matrix is {myMatrix}")
                currentColumn += 1
                if currentColumn >= columns:
                    currentRow+= 1
                    currentColumn = 0
            except:
                continue
    clear()
    print(f"Your final matrix is {myMatrix}")
    return myMatrix