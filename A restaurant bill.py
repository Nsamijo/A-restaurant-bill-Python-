questionsList = ['Please enter the amount you have to pay: ', 'Enter the amount of €100 bill: ',
                 'Enter the amount of €20 bills: ', 'Enter the amount of €1 bills: ']


def getGoodInput(display):
    '''this function returns the amount as an integer and catches bad input'''
    temp = input(display)
    while not temp.isdigit():
        temp = input(display)
    return int(temp)


def askWallet(toAsk):
    '''ask what the user has to pay and the wallet contents'''
    toReturn = []

    def addToList():
        '''add variables to the tuple'''
        toReturn.append(temp)

    for question in toAsk:
        temp = getGoodInput(question)
        addToList()

    return toReturn


def printEnd(ways=0):
    #    print('The amount to pay is: ' + str(amount))
    print('There are ' + str(ways) + ' ways to pay the bill.')


def ableToPay(monnies):
    return monnies[0] <= (monnies[1] * 100 + monnies[2] * 20 + monnies[3] * 1)



monnies = askWallet(questionsList)
if ableToPay(monnies):
    print('Enough money to pay')
else:
    printEnd()