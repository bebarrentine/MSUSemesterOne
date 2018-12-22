# Names: Brianna Barrentine     Date Assigned: 10/25/2018
#
#
# Course: CSE 1284 Sec 12      Date Due:10/25/2018
#
# File name: GradeCalculator
#
# Program Description: It reads a series of numbers from a file (the file should be received as an input from the
# user), keeps a running total, and then averages those numbers to assign a letter grade based on the average

import numpy as np


def main():
    # prints the question statement
    print("What is your file name (with extension)?")

    # prompts the user for the file name
    fileName = input("> ")

    # try block that runs the code within if the file exists
    try:

        # opens the file
        txt = open(fileName)

        # creates the numbers within the file into a list
        with open(fileName) as myGrades:
            grades = [int(x) for x in myGrades.read().split()]

        print("\nReading...\n")

        # prints the numbers within the file with 'Grade #: " in front
        number = 1
        for i in txt:
            print("Grade " + str(number), i, sep=": ")
            number += 1

        # finds and prints the average of the created number list
        gradeAverage = np.mean(grades)
        print("Your grade average is:", gradeAverage)

        # function that determines and prints the letter grade based on the average
        def letterGrade():
            if (90 <= gradeAverage <= 100):
                print("Grade: A")
            elif (80 <= gradeAverage < 90):
                print("Grade: B")
            elif (70 <= gradeAverage < 80):
                print("Grade: C")
            elif (60 <= gradeAverage < 70):
                print("Grade: D")
            else:
                print("You failed")

        letterGrade()

    # runs the code within the exception if the file is not found
    except:
        print("That file does not exist")


# runs the code within the main function
main()
