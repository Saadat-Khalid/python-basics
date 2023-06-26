# Dictionaries
'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets {key:val} , and have keys and values

'''

ma_car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(ma_car["brand"])
print(ma_car)

# Accessing with Key
print(ma_car["brand"])

keys = ma_car.keys() # store the keyss
print(keys)

values = ma_car.values() # storing the values
print(values)

if "colors" in ma_car:
    print("Yes, Colors are avaliable")