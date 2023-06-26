# Type Conversion
# changing an expression from one data type to another.

x = 10      # integer
y = 10.2    # float
z = "Hello" # string

# implicit type conversion

a = x*y # integer * float = float

print(x, "Type  of x is: ", type(x))
print(y, "Type  of y is: ", type(y))
print(z, "Type  of z is: ", type(z))

print(type(a))

# explicit type conversion

age = input("What is your age..??  ")
print(age)
print(age, type(age))

print("Converting the type of Age.....")

age = int(age)
print(age, type(age))

# We can also do in one line..... ;)

age = int(input("What is your Age...? "))
print(age, type(age))

# str() - String, int() - Integer