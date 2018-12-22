# Name: Brianna Barrentine     Date Assigned: 9/27/2018
#
# Course: CSE 1284 Sec 12      Date Due:9/27/2018
#
# File name: LeapYear.py
#
# Program Description: The following program is used to display all of the leap years in the range entered by the user

# This asks the user for a starting year and ending year in order to
# calculate the amount of leap years between the two years
startingYear = int(input("Enter the starting year: "))
endingYear = int(input("Enter the ending year: "))

# The following 'for' loop is what's used to determine and then display which
# years between the start and end years are leap years
for leapYear in range (startingYear, endingYear + 1):
  # Follows the logic: if the year is divisible by 4 it is a leap year
  if leapYear % 4 == 0 and leapYear % 100 != 0:
    print(leapYear)
  # Follows the logic: if the year is divisible by 4, 100, and 400 it is a leap year
  elif leapYear % 4 == 0 and leapYear % 100 == 0 and leapYear % 400 == 0:
    print(leapYear)