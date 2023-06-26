# Functions: A function is simply a “chunk” of code that you can use over and over again, rather than writing it out multiple times.
# syntax

''' def function_name():
    #######
    ########
    ########

funtion_name()
'''
# Method 1

def display_text(): 
    print("I'm Learning Python")
    print("I'm Learning Python")
    print("I'm Learning Python")

display_text() # here we're calling our function...


# Method 2

def display_text():
    some_text = "I'm Learning Python"
    print(some_text)
    print(some_text)
    print(some_text)


display_text()

# Method 3

def display_text(some_text): # here it takes argument in the variable called some_text
    print(some_text)
    print(some_text)
    print(some_text)

    
display_text("I'm Learning Python")


# Function with if - elif - else

def student_grade(marks):

    if marks >= 90:
        print(marks, "Congratulations You Got 'A' Grade.... :) ")

    elif marks >= 80 : 
        print(marks, "Your Grade is 'B'")

    elif marks >= 70 : 
        print(marks, "Your Grade is 'C'")

    elif marks >= 60 : 
        print(marks, "Your Grade is 'D'")

    else: 
        print(marks, "Sorry, study hard next time cuz you got 'F'")

user_marks = int(input("Enter Your Marks?  "))

student_grade(user_marks)


# funtion with return

def addition(add):
    sum = add + 15
    return sum

sum = int(input("Enter Your Number it'll be added with 15:  "))

print(addition(sum))