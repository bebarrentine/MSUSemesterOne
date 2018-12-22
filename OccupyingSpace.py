# Name: Brianna Barrentine     Date Assigned: 9/20/2018
#
# Course: CSE 1284 Sec 12      Date Due:9/20/2018
#
# File name: OccupyingSpace.py
#
# Program Description: The following program is used to determine if a coordinate point is within a specified region.
# This is used to simulate a problem found in graphics: determining when objects occupy the same space.

# this imports turtle allowing the use of functions provided by the turtle library
import turtle

# Gets user input for the following variables in order to determine the location of
# the coordinate within the created rectangle
bottomLeftX = int(input("Enter the x coordinate of the lower lefthand corner of the rectangle:"))
bottomLeftY = int(input("Enter the y coordinate of the lower lefthand corner of the rectangle:"))
height = int(input("Enter the height of the rectangle:"))
width = int(input ("Enter the width of the rectangle:"))
pointX = int(input("Enter the x coordinate of the point:"))
pointY = int(input("Enter the y coordinate of the point:"))

# Creates the variables a and b to be used as representations of
# other points on the rectangle
a = int(bottomLeftY + height)
b = int(bottomLeftX + width)

# The following if,elif statements are the logic determining the
# location of the coordinate point. Stating if the coordinate is
# between a certain set of points then it is either within, on, or outside of the rectangle
if (bottomLeftX < pointX < b) and (bottomLeftY < pointY < a):
  print("The point is inside the rectangle")
elif (bottomLeftX <= pointX <= a) and (bottomLeftX <= pointY <= a):
  print("The point is on the rectangle")
elif (bottomLeftX <= pointX <= b) and (bottomLeftX <= pointY <= b):
  print("The point is on the rectangle")
elif (b <= pointX <= a) and (b <= pointY <= a):
  print("The point is on the rectangle")
else:
  print("The point is not inside the rectangle")

# Creates the two 'turtles' to draw the box and coordinate
turtBox = turtle.Turtle()
turtDot = turtle.Turtle()

# Draws the box
turtBox.color("maroon")
turtBox.penup()
turtBox.goto(bottomLeftX, bottomLeftY)
turtBox.pendown()
turtBox.goto(bottomLeftX, a)
turtBox.pendown()
turtBox.goto(b, a)
turtBox.pendown()
turtBox.goto(b, bottomLeftY)
turtBox.pendown()
turtBox.goto(bottomLeftX, bottomLeftY)

# Draws the coordinate
turtDot.color("gray")
turtDot.pensize(10)
turtDot.penup()
turtDot.goto(pointX, pointY)
turtDot.pendown()

turtle.done()
