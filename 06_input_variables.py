# Input Variables: used to take input from the user 
# Input function is always in string form if you are required numerical value of the input you must convert.

my_favorite_fruit = "Mangoes"
print(my_favorite_fruit) # prints Mangoes

# Input Function
my_favorite_fruit = input("What is your favourite fruit?  ")
print(my_favorite_fruit)

# Input Function of 2nd Stage

name = input("What is your name?  ")
greetings = "Hello !!!"

print(greetings, name)

# 3rd Stage 
name = input("What is your name?  ")
age = int(input("How old are you? ")) # the type will be str because the input is always in str to convert it into number will use int()

print(greetings, name)
