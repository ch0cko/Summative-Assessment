print ("Chapter 1")

print ("\nExercise 1\n")

print ("Twinkle, twinkle, little star, \nHow I wonder what you are! \nUp above the world so high, \nLike a diamond in the sky. \nTwinkle, twinkle, little star, \nHow I wonder what you are")

print ("\nExercise 2\n")

import sys

print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

print ("\nExercise 3\n")

import datetime

date_time = datetime.datetime.now()
print ("Current date and time: ")
print (date_time.strftime("%Y-%m-%d %H:%M:%S"))

print ("\nExercise 4\n")

concat_1 = "Congratulations! "
concat_2 = "You won the top prize, "
concat_3 = "a brand new car"

print (concat_1 + concat_2 + concat_3)

print ("\nExercise 5\n")

import math

pi = math.pi
radius = int(input("Enter the radius of the circle: "))
area = (radius * radius) * pi

print (f"The area of the circle is {area}")

print ("\nChapter 2")

print ("\nExercise 1\n")

message_var = "I am currently in Level 4 Creative Computing"

print (message_var)

message_var = "One of our courses is Introduction to Programming"

print (message_var)

print ("\nExercise 2\n")

print ('Amelia Earhart once said, "The most effective way to do it, is to do it."')

print ("\nExercise 3\n")

name = "\tMarc Allan Raviz\n"

print ("Original: ")
print (name)

print ("\nName with lstrip: ")
print (name.lstrip())

print ("\nName with rstrip: ")
print (name.rstrip())

print ("\nName with strip: ")
print (name.strip())

print ("\nExercise 4\n")

fav_num = 24
print_num = f"{fav_num} is my favorite number."

print (print_num)

print ("\nExercise 5\n")

budget = 50
cost = 6
total = budget // cost
change = budget % total

print (f"The girl can buy {total} USB sticks, and will have a change of ${change}")

print ("\nChapter 3")

print ("\nExercise 1\n")

names = ["Raf", "Andrei", "Wayeth", "JR", "Joshua"]

for name in names:
    print (name)

print ("\nExercise 2\n")

for name in names:
    print (f"Hey {name}! How's your day been?")

print ("\nExercise 3\n")

cars = ["Mitsubishi", "Porsche", "Ferrari", "BMW"]

print (f"I would like to own a {cars[3]}.")
print (f"I like {cars[1]} more than {cars[2]}.")
print (f"My favorite car is a {cars[0]} Lancer Evo.")

print ("\nExercise 4\n")

guest_list = ["Manly", "Sameer", "Rosver"]

for guest in guest_list:
    print (f"Hey {guest}, would you like to come over for dinner?")

print ("\nExercise 5\n")

print ("Manly won't be making it to dinner, I have to invite someone else..\n")

guest_list[0] = "Patrick"

for guest in guest_list:
    print (f"Hey {guest}, would you like to come over for dinner?")

print ("\nExercie 6\n")

print ("I'm sorry, my new table hasn't arrived yet so I can only invite two people.")

popped_guest = guest_list.pop(0)

print (f"\nIm sorry {popped_guest}, I can't invite you over for dinner.\n")

for guest in guest_list:
    print (f"Hey {guest}, don't worry, you are still invited for dinner.")

del guest_list

print ("\nThe list is now empty.")

print ("\nExercise 7\n")

places = ["Niagara Falls", "London", "Amazon Rainforest", "Japan", "Palawan"]

print ("Original order: ")
print (places)

print ("\nAlphabetical order: ")
print (sorted(places))

print ("\nOriginal order: ")
print (places)

print ("\nReverse alphabetical order: ")
print (sorted(places, reverse=True))

print ("\nOriginal order: ")
print (places)

print ("\nReversed order: ")
places.reverse()
print (places)

print ("\nOriginal order: ")
places.reverse()
print (places)

print ("\nAlphabetical order: ")
places.sort()
print (places)

print ("\nReverse alphabetical order: ")
places.sort(reverse=True)
print (places)

print ("\nChapter 4")

print ("\nExercie 1\n")

alien_color = 'green'

if alien_color == 'green':
    print ("You just earned 5 points!")

alien_color = 'red'

if alien_color == 'green':
    print ("You just earned 5 points!")

print ("\nExercise 2\n")

alien_color = 'green'

if alien_color == 'green':
    print ("You just earned 5 points!")

else:
    print ("You just earned 10 points!")

alien_color = 'red'

if alien_color == 'green':
    print ("You just earned 5 points!")

else:
    print ("You just earned 10 points!")

print ("\nExercise 3\n")

alien_color = 'green'

if alien_color == 'green':
    print ("You just earned 5 points!")

elif alien_color == 'yellow':
    print ("You just earned 10 points!")

else:
    print ("You just earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print ("You just earned 5 points!")

elif alien_color == 'yellow':
    print ("You just earned 10 points!")

else:
    print ("You just earned 15 points!")

alien_color = 'red'

if alien_color == 'green':
    print ("You just earned 5 points!")

elif alien_color == 'yellow':
    print ("You just earned 10 points!")

else:
    print ("You just earned 15 points!")

print ("\nExercise 4\n")

age = int(input("Enter your age: "))

if age < 2:
    print ("You are a baby")

elif age < 4:
    print ("You are a toddler")

elif age < 13:
    print ("You are a kid")

elif age < 20:
    print ("You are a teenager")

elif age < 65:
    print ("You are an adult")

else:
    print ("You are an elder")

print ("\nExercise 5\n")

favorite_fruits = ['mangoes', 'jackfruit', 'apples']

if 'strawberries' in favorite_fruits:
    print ("You really like strawberries!")

if 'apples' in favorite_fruits:
    print ("You really like apples!")

if 'oranges' in favorite_fruits:
    print ("You really like oranges!")

if 'dragonfruit' in favorite_fruits:
    print ("You really like dragonfruit!")

if 'jackfruit' in favorite_fruits:
    print ("You really like jackfruit!")

print ("\nChapter 5")

print ("\nExercise 1\n")

person_info = {'first name': 'Wayeth', 'last name': 'Cabanlit', 'age': 18, 'city': 'Sharjah'}

print (person_info['first name'])
print (person_info['last name'])
print (person_info['age'])
print (person_info['city'])

print ("\nExercise 2\n")

glossary = {
    'variable': 'A variable is a symbolic name that is a reference or pointer to an object.', 
    'operator': 'A operator is a symbol that performs an operation on one or more operands.', 
    'for loop': 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).', 
    'list': 'A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.', 
    'function': 'A function is a block of code which only runs when it is called.'
}

for key, value in glossary.items():
    print (f"{key}  -  {value}\n")

print ("Exercise 3\n")

glossary_update = {
    'data types': 'Data types are the classification or categorization of knowledge items.',
    'while loop': 'A while loop is used to run a specific code until a certain condition is met.',
    'dictionary': 'Dictionaries are implementation of a data structure that is more generally known as an associative array.',
    'tuple': 'A tuple is used to store multiple items in a single variable.',
    'lambda': 'A lambda function is an anonymous function that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression.'
}

glossary.update(glossary_update)

for key, value in glossary.items():
    print (f"{key}  -  {value}\n")

print ("Exercise 4\n")

rivers = {
    'nile': 'egypt',
    'amazon': 'south america',
    'murray': 'australia',
    'pasig': 'philippines',
    'shinano': 'japan',
}

for river, country in rivers.items():
    print (f"The {river.title()} River flows through {country.title()}.\n")

print ("\nThe rivers in this dictionary are: \n")

for river in rivers.keys():
    print (f"- {river.title()} River")

print ("\nThe countries in this dictionary are: \n")

for country in rivers.values(): 
    print (f"- {country.title()}")

print ("\nExercise 5")

pet1 = {
    'name': 'ben',
    'type': 'rat',
    'owner': 'michael',
}

pet2 = {
    'name': 'bon-bon',
    'type': 'rabbit',
    'owner': 'andy',
}

pet3 = {
    'name': 'orange',
    'type': 'cat',
    'owner': 'wayeth',
}

pet_list = [pet1, pet2, pet3]

for pet in pet_list:
    print (f"\nInfo about {pet['name'].title()}: ")

    for key, value in pet.items():
        print(f"\t{key}: {str(value).title()}")

print ("\nChapter 6")

print ("\nExercise 1\n")

while True:
    print ("Enter quit when you are finished")
    topping_output = input("What pizza topping would you like? ")

    if topping_output != 'quit':
        print (f"A {topping_output} topping will be added to your pizza.\n")
    
    else:
        print ("\nThank you for ordering a pizza!")
        break

print ("\nExercise 2\n")

movie_ticket = int(input("Enter your age: "))

if movie_ticket < 3:
    print ("\nYour ticket is free.")

elif movie_ticket < 12:
    print ("\nYour ticket costs $10.")

else:
    print ("\nYour ticket costs $15.")

print ("\nExercise 3\n")

infinite = 1

while infinite <= 1000:
    print (infinite)
    infinite += 1

print ("\nExercise 4\n")

sandwich_orders = ['ham', 'seafood', 'grilled cheese', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    progress = sandwich_orders.pop()
    print (f"Please wait, your {progress} sandwich is currently being made.")
    finished_sandwiches.append(progress)

print (" ")

for sandwich in finished_sandwiches:
    print (f"Your order for a {sandwich} has been completed.")

print ("\nExercise 5\n")

sandwich_orders = ['ham', 'seafood', 'grilled cheese', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    progress = sandwich_orders.pop()
    print (f"Please wait, your {progress} sandwich is currently being made.")
    finished_sandwiches.append(progress)

print (" ")

for sandwich in finished_sandwiches:
    print (f"Your order for a {sandwich} has been completed.")

print ("\nChapter 7")

print ("\nExercise 1\n")

