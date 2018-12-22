# Names: Brianna Barrentine     Date Assigned: 11/1/2018
#
#
# Course: CSE 1284 Sec 12      Date Due:11/1/2018
#
# File name: BabyNames.py
#
# Program Description: This program will ask the user for the name of the file
# and then open that file.  It will also prompt the user for a full name and
# gender of the baby name. The program will then search the file for the first
# name in the appropriate column (one column for boys another for girls).  If
# the name is found, the rank for that name will be printed to the screen.

def main():
    print("What is your file name (with extension)?")
    fileName = input("> ")

    year = fileName.split('_')
    year = year[-1].split('.')
    year = year[0]

    try:
        txt = open(fileName, "r")

        print("\nEnter the baby's first and last name:")
        babyName = input("> ")
        babyName = babyName.split()
        babyName = babyName[0]

        print("\nEnter the gender of the baby (m/f)")
        babyGender = input("> ")

        if babyGender == "m":
            for line in txt:
                if line.split()[1] == babyName:
                    print('\n', year, "Rank: ", line.split()[0])


        elif babyGender == "f":
            for line in txt:
                if line.split()[3] == babyName:
                    print('\n', year, "Rank: ", line.split()[0])
        else:
            print("\nPlease select m or f. Try again")

        print("\n\nIf no rank is listed, the name is not ranked in that decade")



    except:
        print("This file does not exist")


main()
