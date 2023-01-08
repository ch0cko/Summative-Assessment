print ("Chapter 1") #prints a string of characters

print ("\nExercise 1\n") #prints a string of characters, '\n' creates a new line, allowing formatting in the output

print ("Twinkle, twinkle, little star, \nHow I wonder what you are! \nUp above the world so high, \nLike a diamond in the sky. \nTwinkle, twinkle, little star, \nHow I wonder what you are")
#'\n' formats the output to be on multiple lines, instead of one, continuous line.

print ("\nExercise 2\n")

import sys #imports constants, functions, and methods of the python interpreter to be called upon by the user

print("Python version")
print (sys.version) #prints the current version of python
print("Version info.")
print (sys.version_info) #prints infromation of the current verion of python

print ("\nExercise 3\n")

import datetime #imports the current date and time data of the system

date_time = datetime.datetime.now() #inputs the date and time data into a variable
print ("Current date and time: ")
print (date_time.strftime("%Y-%m-%d %H:%M:%S")) #prints the current date and time of the system in a proper format

print ("\nExercise 4\n")

concat_1 = "Congratulations! " #stores a string into a variable
concat_2 = "You won the top prize, "
concat_3 = "a brand new car"

print (concat_1 + concat_2 + concat_3) #concatenates the three variables to be printed together as one string

print ("\nExercise 5\n")

import math #imports mathematical constants and functions to be used by the python interpreter

pi = math.pi #inputs the pi constant into a variable
radius = int(input("Enter the radius of the circle: ")) #allows the user to input a number into a variable to be called upon later
area = (radius * radius) * pi #inputs the formula for the area of a circle into a variable

print (f"The area of the circle is {area}") #prints a string, making use of the 'f-string', allowing variables to be placed seamlessly inside the string