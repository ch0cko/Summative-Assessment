print ("\nChapter 2")

print ("\nExercise 1\n")

message_var = "I am currently in Level 4 Creative Computing" #stores a string in a variable

print (message_var) #prints the variable containing the string

message_var = "One of our courses is Introduction to Programming"

print (message_var)

print ("\nExercise 2\n")

print ('Amelia Earhart once said, "The most effective way to do it, is to do it."') #prints a string

print ("\nExercise 3\n")

name = "\tMarc Allan Raviz\n" #stores a string in a variable, '\t' putting a tab space before the string and '\n' creating a new line after it

print ("Original: ")
print (name) #prints the original form of the string

print ("\nName with lstrip: ")
print (name.lstrip()) #removes whitespace on the left of the string

print ("\nName with rstrip: ")
print (name.rstrip()) #removes whitespace on the right of the string

print ("\nName with strip: ")
print (name.strip()) #removes whitespace on both the left and right of the string

print ("\nExercise 4\n")

fav_num = 24 #stores the number '24' in a variable
print_num = f"{fav_num} is my favorite number." #makes use of the 'f-string' to seamlessly insert the aforementioned variable into a string, which itself is inside a variable

print (print_num) #prints a variable containing a string

print ("\nExercise 5\n")

budget = 50 #stores a numerical value inside a variable
cost = 6
total = budget // cost #stores a division formula inside a variable
change = budget % total #stores a modulus formula inside a variable

print (f"The girl can buy {total} USB sticks, and will have a change of ${change}") #prints a string, making use of the 'f-string' to insert variables into the string