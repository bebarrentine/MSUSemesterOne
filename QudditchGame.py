# Name: Brianna Barrentine     Date Assigned: 9/13/2018
#
# Course: CSE 1284 Sec 12      Date Due:9/13/2018
#
# File name: QudditchGame.py
#
# Program Description: The following program uses inputs from the user to determine the outcome of a fictional
# quidditch game.

print("---+---+Welcome to CSE 1284 Quidditch Statistics Calculator+---+---\n")

print("Just provide us with the teams, end score, and match time and we'll do the rest!\n\n")

# This portion of the code requests all the user's inputs for calculating the statistics
teamOne = input("Enter the name of the team that caught the golden snitch:")
teamOneScore = int(input("Enter the previously mentioned team's final score:"))
print("")
teamTwo = input("Enter the name of the competing team:")
teamTwoScore = int(input("Enter this team's final score:"))
print("")
matchTime = int(input("Enter the length of the match in minutes:"))

# This portion of the code calculates the statistics
teamOneGoals = int((teamOneScore - 150) / 10)
if teamOneGoals <= 0:
    teamOneGoals = 0
teamTwoGoals = int(teamTwoScore / 10)
teamOneGPM = float(teamOneGoals / matchTime)
teamTwoGPM = float(teamTwoGoals / matchTime)

# This prints the final statistics for Team One
print("")
print("Team One's Statistics:")
print("========================")
print("House:", teamOne)
print("Goals:", teamOneGoals)
print("Snitch: 1")
print("Goals Per Minute:", teamOneGPM)

# This prints the final statistics for Team Two
print("")
print("Team Two's Statistics:")
print("========================")
print("House:", teamTwo)
print("Goals:", teamTwoGoals)
print("Snitch: 0")
print("Goals Per Minute:", teamTwoGPM)
