import random
import sys


def main():
    startGame = 'y'

    while startGame == 'y':

        def getDeck():
            return random.randint(0, 51)

        def getCardValue(card):

            faceValue = int(card / 4) + 1
            suit = card % 4

            if (faceValue == 0):
                faceValue = ""
            elif (faceValue == 1):
                faceValue = "A"
            elif (faceValue == 11):
                faceValue = "J"
            elif (faceValue == 12):
                faceValue = "Q"
            elif (faceValue == 13):
                faceValue = "K"
            else:
                faceValue = str(faceValue)

            if (suit == 0):
                suit = " Clubs "
            elif (suit == 1):
                suit = " Diamonds "
            elif (suit == 2):
                suit = " Hearts "
            elif (suit == 3):
                suit = " Spades "
            else:
                suit = ""
            print("Error! Bad suit")

            return faceValue + suit

        def scoreHand(card1, card2, card3):
            score = 0
            faceValue1 = int(card1 / 4) + 1
            faceValue2 = int(card2 / 4) + 1
            faceValue3 = 0

            if card3 != -1:
                faceValue3 = int(card3 / 4) + 1

            if faceValue1 == 0:
                score1 = 0
            elif faceValue1 == 1:
                score1 = 11
            elif faceValue1 == 11 or faceValue1 == 12 or faceValue1 == 13:
                score1 = 10
            else:
                score1 = faceValue1

            if faceValue2 == 0:
                score2 = 0
            elif faceValue2 == 1:
                score2 = 11
            elif faceValue2 == 11 or faceValue2 == 12 or faceValue2 == 13:
                score2 = 10
            else:
                score2 = faceValue2

            if faceValue3 == 0:
                score3 = 0
            elif faceValue3 == 1:
                score3 = 11
            elif faceValue3 == 11 or faceValue3 == 12 or faceValue3 == 13:
                score3 = 10
            else:
                score3 = faceValue3

            score = score1 + score2 + score3
            return score

        def newCard():
            promptNew = input("Would you like one more card? (y/n) ")
            while (promptNew != 'y' and promptNew != 'n'):
                print("Please enter 'y' or 'n'")
                promptNew = input("Would you like one more card? (y/n) ")

            if promptNew == 'y':
                return getDeck()
            else:
                return -1

        if startGame == 'y':

            userCard1 = getDeck()
            userCard2 = getDeck()
            userCard3 = -1
            computerCard1 = getDeck()
            computerCard2 = getDeck()
            computerCard3 = -1

            print("User:", getCardValue(userCard1), "", getCardValue(userCard2), end='')

            if (userCard3 != -1):
                print("", getCardValue(userCard3), end='')

            print("\nComputer:", getCardValue(computerCard1), "", getCardValue(computerCard2), end='')

            if (computerCard3 != -1):
                print("", getCardValue(computerCard3), end='')

            print("\n")

            userScore = scoreHand(userCard1, userCard2, userCard3)
            computerScore = scoreHand(computerCard1, computerCard2, computerCard3)
            userCard3 = newCard()

            if (userScore > computerScore and userScore <= 21):
                computerCard3 = getDeck()

            print("User:", getCardValue(userCard1), "", getCardValue(userCard2), end='')

            if (userCard3 != -1):
                print("", getCardValue(userCard3), end='')

            print("\nComputer:", getCardValue(computerCard1), "", getCardValue(computerCard2), end='')

            if (computerCard3 != -1):
                print("", getCardValue(computerCard3), end='')

            print("\n")

            computerScore = scoreHand(computerCard1, computerCard2, computerCard3)

            print("User score: ", userScore)
            print("Computer score: ", computerScore)

            if (userScore < 21):
                print("Busted!")
            elif (userScore == computerScore):
                print("It's a tie")
            elif (computerScore <= 21 and computerScore > userScore):
                print("Sorry. You lost!")
            else:
                print("Congratulations! You won.")

            playResponse = input("Do you want to play again?")

            while (playResponse != 'y' and playResponse != 'n'):
                print("Please enter only a 'y' or 'n'")
                playResponse = input("Do you want to play again?")

            if playResponse == 'y':
                startGame = 'y'

            else:
                startGame = 'n'

# I have no idea how to play blackjack...
main()