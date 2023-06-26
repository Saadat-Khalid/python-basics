# trouble shooting 
# error handling
# how to handle the error

'''
print(we are learning python) # Syntax error
print(30/0) # runtime error Mathimatical Error(ZeroDivisionError) 

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

'''
try:
    num = 30/0
    print(num) # this will throw an error but will be handled by except
except:
    print("An exception occurred")

