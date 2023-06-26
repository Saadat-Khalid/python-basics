#Sets
'''
A set is a collection which is unordered, unchangeable*, and unindexed.
Sets are written with curly brackets {}

'''

thisset = {"apple", "banana", "cherry"}
print(thisset) 

# can't be accessed with index or key like list, tuples, & dictionary
# you have to loop through it

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print("cherry" in thisset) # to check if the cheery is present in our set
  print(x)

