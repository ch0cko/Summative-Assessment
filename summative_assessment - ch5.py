print ("\nChapter 5")

print ("\nExercise 1\n")

person_info = {'first name': 'Wayeth', 'last name': 'Cabanlit', 'age': 18, 'city': 'Sharjah'} #creates a dictionary containing keys and values

print (person_info['first name']) #prints a specific item in the dictionary
print (person_info['last name']) #prints a specific item in the dictionary
print (person_info['age']) #prints a specific item in the dictionary
print (person_info['city']) #prints a specific item in the dictionary

print ("\nExercise 2\n")

glossary = { #creates a dictionary containing keys and values
    'variable': 'A variable is a symbolic name that is a reference or pointer to an object.', 
    'operator': 'A operator is a symbol that performs an operation on one or more operands.', 
    'for loop': 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).', 
    'list': 'A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.', 
    'function': 'A function is a block of code which only runs when it is called.'
}

for key, value in glossary.items(): #loops and prints through all the items in the dictionary
    print (f"{key}  -  {value}\n") #uses the f-string function to format the keys and values in a string

print ("Exercise 3\n")

glossary_update = { #creates a dictionary containing keys and values
    'data types': 'Data types are the classification or categorization of knowledge items.',
    'while loop': 'A while loop is used to run a specific code until a certain condition is met.',
    'dictionary': 'Dictionaries are implementation of a data structure that is more generally known as an associative array.',
    'tuple': 'A tuple is used to store multiple items in a single variable.',
    'lambda': 'A lambda function is an anonymous function that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression.'
}

glossary.update(glossary_update) #updates the original dictionary with the new items

for key, value in glossary.items(): #loops and prints through all the items in the dictionary
    print (f"{key}  -  {value}\n") #uses the f-string function to format the keys and values in a string

print ("Exercise 4\n")

rivers = { #creates a dictionary containing keys and values
    'nile': 'egypt',
    'amazon': 'south america',
    'murray': 'australia',
    'pasig': 'philippines',
    'shinano': 'japan',
}

for river, country in rivers.items(): #loops and prints through all the items in the dictionary
    print (f"The {river.title()} River flows through {country.title()}.\n") #uses the f-string function to format the keys and values in a string

print ("\nThe rivers in this dictionary are: \n")

for river in rivers.keys(): #loops and prints only the keys in the dictionary
    print (f"- {river.title()} River") #uses the f-string function to format the keys and values in a string

print ("\nThe countries in this dictionary are: \n")

for country in rivers.values(): #loops and prints only the values in the dictionary
    print (f"- {country.title()}") #uses the f-string function to format the keys and values in a string

print ("\nExercise 5")

pet1 = { #creates a dictionary containing keys and values
    'name': 'ben',
    'type': 'rat',
    'owner': 'michael',
}

pet2 = { #creates a dictionary containing keys and values
    'name': 'bon-bon',
    'type': 'rabbit',
    'owner': 'andy',
}

pet3 = { #creates a dictionary containing keys and values
    'name': 'lulu',
    'type': 'cat',
    'owner': 'wayeth',
}

pet_list = [pet1, pet2, pet3] #stores all the dictionaries in the list

for pet in pet_list: #prints all the items in the list
    print (f"\nInfo about {pet['name'].title()}: ")

    for key, value in pet.items(): #prints the specific keys and values listed inside the dictionaries
        print(f"\t{key}: {str(value).title()}")