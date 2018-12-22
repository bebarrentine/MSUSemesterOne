# Name: Brianna Barrentine              Date Assigned: 10/4/2018
#
#
# Course: CSE 1284 Sec 12               Date Due:10/4/2018
#
# File name: DrawingDiamonds.py
#
# Program Description: The following code will draw a diamond-shaped picture by taking the user's input. This input
# determines the number of lines to be drawn.

# prompts the user for a number to represent the variable diamondHeight
print("---------Stage 1---------")
diamondHeight = int(input("Enter the height of the diamond:"))

# This while loop prevents the user from inputting a number an even and/or negative number by displaying an error
# code and prompting them for a new number
while diamondHeight % 2 == 0 or diamondHeight <= 0:
  print("ERROR: The height must be an odd number greater than 0")
  diamondHeight = int(input("Please re-enter:"))

# prints the statement when the heaight is a validated number
print("The validated height of the diamond is",diamondHeight,"\n")

print("---------Stage 2---------")
print('')
a = 1
for a in range(diamondHeight + 1):
  top = (diamondHeight - a)
  print ("*"*(a) + " "*top)
print('')

print("---------Stage 3---------")
print('')
a = 1
for a in range(diamondHeight + 1):
  if a%2 != 0:
    top = (diamondHeight - a)//2
    print ("* "*((a // 2) + 1))# + " "*top)
print('')


print("---------Stage 4---------")
print('')
a = 1
for a in range(diamondHeight + 1):
    if a%2 != 0:
        top = (diamondHeight - a) // 2
        print (" "*(top*2) + "* "*(a) + " "*(a-1) +" "*top)
print('')

print("---------Stage 5---------")
print('')
a = 1 # a placeholder variable used to solve the top half of the diamond
b = 1 # a placeholder variable used to solve the bottom half of the diamond

# This for loop produces the top half of the diamond by alternating astracts and spaces
for a in range(diamondHeight + 1):
    if a%2 != 0:
        top = (diamondHeight - a) // 2
        print (" "*top*2 + "* "*(a) + " "*top)

# This for loop produces the bottom half of the diamond by alternating astracts and spaces
for b in range(diamondHeight - 1,0,-1):
    if b%2 != 0:
        bot = (diamondHeight-b)//2
        print (" "*bot*2 + "* "*(b) + " "*bot)