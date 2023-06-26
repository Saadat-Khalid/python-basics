# Lambda

'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

lambda arguments : expresion
'''

x = lambda a : a+15

print(x(5))

power = lambda x : x**2

print(power(5))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(2))

