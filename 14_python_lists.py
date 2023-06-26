# Listis

'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data
Lists are created using square brackets []

'''
basket = ["apple", "banana", "cherry"]
print(basket)

print(len(basket)) # len() to check the length

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

print(list1)
print(list2)
print(list3)
print(list4)

# I want to access only "cherry" from list1
# list[index_of_item_you_want_to_access] 

print(list1[2])
print(list1[-1]) # this is negative indexing
print(list1[1:]) # Range indexing (if I want to access only 'Banana', 'Cherry')

# list with loop

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    print(d)
