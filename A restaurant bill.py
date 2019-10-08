questionsList = ['Please enter the amount you have to pay: ', 'Enter the amount of €100 bill: ',
                 'Enter the amount of €20 bills: ', 'Enter the amount of €1 bills: ']
# default values used
DEFAULT_VALUE_100 = 100
DEFAULT_VALUE_20 = 20
DEFAULT_VALUE_1 = 1
# variable which will contain the amount to pay
toPay = 0


def getGoodInput(display):
    '''this function returns the amount as an integer and catches bad input'''
    temp = input(display)
    while not temp.isdigit() and not (temp == 'exit'):
        temp = input(display)
    if temp == 'exit':
        return '#'
    else:
        return int(temp)


def askWallet(toAsk):
    '''ask what the user has to pay and the wallet contents '''
    toReturn = []

    def addToList():
        '''add variables to the list'''
        toReturn.append(temp)

    for question in toAsk:
        temp = getGoodInput(question)
        if '#' == temp:
            return '#'
        addToList()

    return toReturn


def printEnd(ways=0):
    '''print the number of ways to pay the bill'''
    #    print('The amount to pay is: ' + str(amount))
    if ways == 1:
        print('There is 1 way to pay the bill')
    else:
        print('There are ' + str(ways) + ' ways to pay the bill.')


def ableToPay(monnies):
    '''checking if there is enough money to pay the bill'''
    return monnies[0] <= (monnies[1] * 100 + monnies[2] * 20 + monnies[3] * 1)


def extractAmountToPay():
    '''the amount is extracted from the list'''
    global toPay, monnies
    toPay = monnies[0]
    del (monnies[0])
    return


def printAllDifferentWaysToPay():
    '''print all the different ways that the user van pay'''
    global waysToPay
    for x in waysToPay:
        print(str(x[0]) + ' x 100, ' + str(x[1]) + ' x 20, ' + str(x[2]) + ' x 1')


def calculateWaysToPay(monnies):
    '''Calculate the ways that the user is able to pay the bills and returns a list'''
    global DEFAULT_VALUE_100, DEFAULT_VALUE_20, DEFAULT_VALUE_20, toPay
    returnVar = []

    def calculate(hundred, twenties, dollars):
        '''This function calculates if the given way is able to pay'''
        toReturn = []
        for hun in range(hundred + 1):
            for twen in range(twenties + 1):
                for doll in range(dollars + 1):
                    total = DEFAULT_VALUE_100 * hun + DEFAULT_VALUE_20 * twen + DEFAULT_VALUE_1 * doll
                    if total == toPay:
                        toReturn.append([hun, twen, doll])
                    #  print(str([usableHundred, usableTwenties, usableDollars]))

        return toReturn

    hundreds, twenties, dollars = monnies
    returnVar = calculate(hundreds, twenties, dollars)

    return returnVar


# main
while True:
    monnies = askWallet(questionsList)
    if '#' in monnies:
        break
    if ableToPay(monnies):
        extractAmountToPay()
        temp = calculateWaysToPay(monnies)
        if isinstance(temp, list):
            waysToPay = temp

        intWaysToPay = len(waysToPay)
        printEnd(intWaysToPay)
        printAllDifferentWaysToPay()
    else:
        printEnd()