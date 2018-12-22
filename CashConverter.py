# Names: Brianna Barrentine     Date Assigned: 11/8/2018
#
#
# Course: CSE 1284 Sec 12      Date Due:11/8/2018
#
# File name: CashConverter.py
#
# Program Description: The following program takes an input of a cash value and
# then converts and prints it into however many bills and coins are needed to
# equal this amount

def main():
    print(
        "Hello! Welcome to the currency calculator.\nEnter in a valid price (in decimal) and we'll tell you how much "
        "of each bill and coin you'll need to best meet that amount.\n")

    print("Enter in a price:")

    # This while statements continues to run until a valid input is made (ie. integers that represent cash value)
    while True:
        try:
            moneyAmount = float(input('> '))
        except:
            print("That wasn't a valid price!")
            continue
        else:
            break

    # converts the users input to a string to be split into dollars and cents
    moneyAmount = str(moneyAmount)

    # splitd the string on the decimal point
    billsSplit = moneyAmount.split('.')

    # assigns the seperate indexes of the splitted string to bills and cents
    bills = billsSplit[0]
    cents = billsSplit[1]

    # converts the string back to an integer
    bills = int(bills)
    cents = int(cents)

    # this function does the actual calculations of how many bills are needed
    def calcBills(bills):
        numHundreds = 0
        numFifties = 0
        numTwenties = 0
        numTens = 0
        numFives = 0
        numOnes = 0

        # calculates how many hundred dollar bills are needed and then subtract
        # from the original amount to solve for the rest of the bills (pattern
        # continues until it reaches one dollar bills)
        numHundreds = bills // 100
        bills = bills - numHundreds * 100

        numFifties = bills // 50
        bills = bills - numFifties * 50

        numTwenties = bills // 20
        bills = bills - numTwenties * 20

        numTens = bills // 10
        bills = bills - numTens * 10

        numFives = bills // 5
        bills = bills - numFives * 5

        numOnes = bills // 1
        bills = bills - numOnes

        # defines the variables within the displayBills function
        displayBills(numHundreds, numFifties, numTwenties, numTens, numFives, numOnes)

    # Uses calculations from calcBills to cleanly display bill amounts
    def displayBills(numHundreds, numFifties, numTwenties, numTens, numFives, numOnes):
        print('')
        print("The paper bills you will need:\n")
        print(numHundreds, "Hundreds")
        print(numFifties, "Fifties")
        print(numTwenties, "Twenties")
        print(numTens, "Tens")
        print(numFives, "Fives")
        print(numOnes, "Ones\n")

    # this function does the actual calculations of how many coins are needed
    def calcCents(cents):
        numQuarters = 0
        numDimes = 0
        numNickels = 0
        numPennies = 0

        # calculates how many quarters are needed and then subtracts
        # from the original amount to solve for the rest of the coins (pattern
        # continues until it reaches pennies)
        numQuarters = cents // 25
        cents = cents - numQuarters * 25

        numDimes = cents // 10
        cents = cents - numDimes * 10

        numNickels = cents // 5
        cents = cents - numNickels * 5

        numPennies = cents // 1
        cents = cents - numPennies

        # defines the variables within the displayCents function
        displayCents(numQuarters, numDimes, numNickels, numPennies)

    # Uses calculations from calcBills to cleanly display coin amounts
    def displayCents(numQuarters, numDimes, numNickels, numPennies):
        print("The coins you will need:\n")
        print(numQuarters, "Quarters")
        print(numDimes, "Dimes")
        print(numNickels, "Nickels")
        print(numPennies, "Pennies")

    # runs the functions to do the calculations
    calcBills(bills)
    calcCents(cents)


# runs code within main function
main()