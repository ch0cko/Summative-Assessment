print ("\nChapter 7")

print ("\nExercise 1\n")

def display_message(): #creates a function
    message = "This chapter is about storing code in functions." #stores a string in a variable
    print (message) #prints the string stored in the variable

display_message() #calls the function 

print ("\nExercise 2\n")

def favorite_book(title): #cretaes a function
    print (f"{title} is my favorite book") #prints a statement

favorite_book('Eragon') #calls the function and adds to its parameters

print ("\nExercise 3\n")

def make_shirt(size, message): #creates a function
    print (f"The shirt I'm making is {size}.")
    print (f"The message '{message}' is going to be printed on the shirt\n")

make_shirt ('extra-large', 'Keyboard Warrior') #calls the function and changing its given values
make_shirt (size = "small", message = 'Flat Earther') #calls the function and changing its given values

print ("Exercise 4\n")

def make_shirt(size = 'large', message = 'I love Python!'): #creates a function
    print (f"The shirt I'm making is {size}.") 
    print (f"The message '{message}' is going to be printed on it.\n")

make_shirt () #calls the function and changing its given values
make_shirt (size = 'medium')
make_shirt ('extra-large', 'Wooting Keyboard Buff')

print ("Exercise 5\n")

def describe_city(city, country = 'united arab emirates'): #creates a function
    city = f"The city {city.title()} is in the country {country.title()}\n"
    print(city)

describe_city('sharjah') #calls the function and changing its given values
describe_city('antipolo', 'philippines')
describe_city('abu dhabi')