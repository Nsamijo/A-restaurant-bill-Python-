questionsList = ['Please enter the amount you have to pay: ', 'Enter the amount of €100 bill: ',
                 'Enter the amount of €20 bills: ', 'Enter the amount of €1 bills: ']
DEFAULT_VALUE_100 = 100
DEFAULT_VALUE_20 = 20
DEFAULT_VALUE_1 = 1

DEFAULT_100_TO_1 = 100
DEFAULT_100_TO_20 = 5
DEFAULT_20_TO_1 = 20
toPay = 0


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
        '''add variables to the list'''
        toReturn.append(temp)

    for question in toAsk:
        temp = getGoodInput(question)
        addToList()

    return toReturn


def printEnd(ways=0):
    '''print the number of ways to pay the bill'''
    #    print('The amount to pay is: ' + str(amount))
    if ways == 1:
        print('There is 1 ways to pay the bill')
    else:
        print('There are ' + str(ways) + ' ways to pay the bill.')



def ableToPay(monnies):
    '''checking if there is enough money to pay the bill'''
    return monnies[0] <= (monnies[1] * 100 + monnies[2] * 20 + monnies[3] * 1)


def extractAmountToPay():
    '''the amount is extracted from the list'''
    global toPay, monnies
    toPay = monnies[0]
    del(monnies[0])
    return

def printAllDifferentWaysToPay(listOfWaysToPay):
    '''print all the different ways that the user van pay'''
    global waysToPay
    for x in waysToPay:
        print( str(x[0]) + ' x 100, ' + str(x[1]) + ' x 20, ' + str(x[2]) + ' x 1')


def calculateWaysToPay(monnies):
    '''Calculate the ways that the user is able to pay the bills and returns a list'''
    global DEFAULT_100_TO_1, DEFAULT_100_TO_20, DEFAULT_20_TO_1, DEFAULT_VALUE_100, DEFAULT_VALUE_20, DEFAULT_VALUE_20, toPay
    returnVar = []

    def availableBills(want, available):
        '''Check if the bills that are needed are available'''
        return want >= available

    def calculate(hundred, twenties, dollars, billList):
        '''This function calculates if the given way is able to pay'''
        temp = toPay
        usableHundred = temp // DEFAULT_VALUE_100

        if not availableBills(usableHundred, hundreds):
            if hundreds < billList[0]:
                temp = temp + (billList[0] - hundreds) * DEFAULT_VALUE_100
                usableHundred = hundreds

        temp = temp - (DEFAULT_VALUE_100 * usableHundred)
        usableTwenties = temp // DEFAULT_VALUE_20

        if not availableBills(usableTwenties, twenties):
            if twenties < billList[1]:
                temp = temp + (billList[1] - twenties) * DEFAULT_VALUE_20
                usableTwenties = twenties

        temp = temp - (DEFAULT_VALUE_20 * usableTwenties)
        usableDollars = temp // DEFAULT_VALUE_1

        if ableToPay([toPay, usableHundred, usableTwenties, usableDollars]) and (usableHundred * DEFAULT_VALUE_100 + usableTwenties * DEFAULT_VALUE_20 + usableDollars * DEFAULT_VALUE_1 == toPay):
            return [usableHundred, usableTwenties, usableDollars]
        else:
            return 0

    hundreds, twenties, dollars = monnies
    defaultBills = monnies
    while hundreds > 0 or twenties > 0 or dollars > 0:
        temp = calculate(hundreds, twenties, dollars, monnies)
        '''check if the function returns a list'''
        if isinstance(temp, list) and not (temp in returnVar):
            returnVar.append(temp)

        if hundreds > 0:
            hundreds = hundreds - 1
        elif twenties > 0:
            twenties = twenties - 1
        elif dollars > 0:
            dollars = dollars - 1

    return returnVar

monnies = askWallet(questionsList)
if ableToPay(monnies):
    extractAmountToPay()
    temp = calculateWaysToPay(monnies)
    if isinstance(temp, list):
        waysToPay = temp
    intWaysToPay = len(waysToPay)

    printEnd(intWaysToPay)
    printAllDifferentWaysToPay(waysToPay)
else:
    printEnd()