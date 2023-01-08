print ("\nChapter 3")

print ("\nExercise 1\n")

names = ["Raf", "Andrei", "Wayeth", "JR", "Joshua"] #stores items in a list

for name in names: #loops through the contents of the list, displaying all its contents
    print (name) 
print ("\nExercise 2\n")

for name in names: #loops through the contents of the list, this time with each individual item put inside of a string with the use of the 'f-string'
    print (f"Hey {name}! How's your day been?") 

print ("\nExercise 3\n")

cars = ["Mitsubishi", "Porsche", "Ferrari", "BMW"] #stores items in a list

print (f"I would like to own a {cars[3]}.") #prints the 4th item in the list inside a string
print (f"I like {cars[1]} more than {cars[2]}.") #prints the 2nd and 3rd items in the list inside a string
print (f"My favorite car is a {cars[0]} Lancer Evo.") #prints the 1st item in the list inside a string

print ("\nExercise 4\n")

guest_list = ["Manly", "Sameer", "Rosver"] #stores items inside a list

for guest in guest_list: #loops through all the items in a list, printing the items as a string
    print (f"Hey {guest}, would you like to come over for dinner?")

print ("\nExercise 5\n")

print ("Manly won't be making it to dinner, I have to invite someone else..\n") #prints a string

guest_list[0] = "Patrick" #replaces an item to the list

for guest in guest_list: #loops through all the items in a list, printing the items as a string
    print (f"Hey {guest}, would you like to come over for dinner?")

print ("\nExercie 6\n")

print ("I'm sorry, my new table hasn't arrived yet so I can only invite two people.") #prints a string

popped_guest = guest_list.pop(0) #pops an item on the list, removing it, not permanently deleting it

print (f"\nIm sorry {popped_guest}, I can't invite you over for dinner.\n") #prints a string

for guest in guest_list: #loops through the list, printing a string one by one, containing an item from the list
    print (f"Hey {guest}, don't worry, you are still invited for dinner.")

del guest_list #deletes the contents of the list

print ("\nThe list is now empty.")

print ("\nExercise 7\n")

places = ["Niagara Falls", "London", "Amazon Rainforest", "Japan", "Palawan"] #stores items in a list

print ("Original order: ")
print (places) #prints the list in its original order

print ("\nAlphabetical order: ")
print (sorted(places)) #sorts the list in alphabetical order

print ("\nOriginal order: ")
print (places) #prints the list as is

print ("\nReverse alphabetical order: ")
print (sorted(places, reverse=True)) #sorts the list in reverse alphabetical order

print ("\nOriginal order: ")
print (places) #prints the list as is

print ("\nReversed order: ")
places.reverse() #reverses the list
print (places) #prints the list in its original order but in reverse

print ("\nOriginal order: ")
places.reverse() #reverses the list
print (places) #prints the list in its original order, now that it has been reversed twice

print ("\nAlphabetical order: ")
places.sort() #sorts the list in alphabetical order permanently
print (places) #prints the list

print ("\nReverse alphabetical order: ")
places.sort(reverse=True) #sorts the list in reverse alphabetical order permanently
print (places) #prints the list