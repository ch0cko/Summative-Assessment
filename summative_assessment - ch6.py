print ("\nChapter 6")

print ("\nExercise 1\n")

while True: #creates a while loop
    print ("Enter quit when you are finished") #prints a string
    topping_output = input("What pizza topping would you like? ") #allows the user to input a string to be stroed into a variable

    if topping_output != 'quit': #if the input is NOT 'quit', prints as string and continues the loop
        print (f"A {topping_output} topping will be added to your pizza.\n")
    
    else: #prints a string then ends the loop
        print ("\nThank you for ordering a pizza!")
        break

print ("\nExercise 2\n")

movie_ticket = int(input("Enter your age: ")) #allows the user to input a number into a variable

if movie_ticket < 3: #prints a string if the input is less than 3
    print ("\nYour ticket is free.")

elif movie_ticket < 12: #prints a string if the input is less than 12
    print ("\nYour ticket costs $10.")

else: #prints a string if none of the previous parameters were met
    print ("\nYour ticket costs $15.")

print ("\nExercise 3\n")

infinite = 1 #stores a number in the variable

while infinite <= 1000: #creates a while loop that continuously increases the original value (only added a cap/limit so the rest of the chapter's code can be run)
    print (infinite)
    infinite += 1 #increases the original value of the number in the variable

print ("\nExercise 4\n")

sandwich_orders = ['ham', 'seafood', 'grilled cheese', 'chicken'] #creates a list
finished_sandwiches = [] #empty list

while sandwich_orders: #creates a while loop
    progress = sandwich_orders.pop() #stores popped items in a variable
    print (f"Please wait, your {progress} sandwich is currently being made.")
    finished_sandwiches.append(progress) #prints all the popped items from the list

print (" ")

for sandwich in finished_sandwiches: #creates a for loop for the finished items in the list
    print (f"Your order for a {sandwich} has been completed.")

print ("\nExercise 5\n")

sandwich_orders = ['pastrami', 'ham', 'seafood', 'pastrami', 'grilled cheese', 'pastrami', 'chicken'] #creates a list
finished_sandwiches = [] #empty list

print ("Sorry, but we no longer have any pastrami on stock today. We won't be able to fulfil and orders for pastrami sandwiches.\n") #prints a string

while 'pastrami' in sandwich_orders: #creates a while loop
    sandwich_orders.remove('pastrami') #removes items from the list

while sandwich_orders: #creates a while loop
    progress = sandwich_orders.pop() #stores popped items in a variable
    print (f"Please wait, your {progress} sandwich is currently being made.")
    finished_sandwiches.append(progress) #prints all the popped items from the list

print (" ")

for sandwich in finished_sandwiches: #creates a for loop for the finished items in the list
    print (f"Your order for a {sandwich} has been completed.")