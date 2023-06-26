# Loops
# A for loop is used for iterating over a sequence
# There are 2 types of Loop 1- For Loop, 2- While Loop

# While Loop

even_num = 2

while (even_num  <= 20):
    print(even_num )
    even_num += 2

print("\n")

# For Loop
# odd number
for a in range(3,20,2): # range(start,stop,step)
    print(a)

# Lists

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    print(d)

for d in days:
    if d == "Fri": break # this will break the loop
    print(d)