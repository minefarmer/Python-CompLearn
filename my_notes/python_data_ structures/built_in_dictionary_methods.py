'''             BUILT-IN DICTIONARY METHODS
Method      Description
get()       Returns the value of specified key.
update()    Inserts a specified key:value pair in dictionary
clear()     Removes all key:value pairs
keys()      Returns a list of dictionary keys.
del()       Deletes the dictionary.

        Some other functions I can use.
Count key:value pairs by using the len function.    line: 33
How to change the value of a key.                   line: 35
How to return the value of a specified key.         line: 38
How to add a new key:value pair.                    line: 40
Keys method will return a list of all the Keys.     line: 43
Values method will return a list of all thevalues.  line: 46
To remove a value I can use pop or delete.          line: 49
del mycar["color"] # removes an item pair.          line: 52
To empty the dictionary use the method 'clear'      line: 55
The delete method will completly delete the dict.   line: 58
'''
mycar = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}

print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2017}

mygreens = dict(fruit="green apples", vegetables="kale")

print(mygreens)  # {'fruit': 'green apples', 'vegetables': 'kale'}

print(len(mycar))  # 3

mycar["year"] = 2022
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2022}

print(mycar.get("year"))  # 2022

mycar.update({"color": "silver"})
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2022, 'color': 'silver'}

b = mycar.keys()
print(b)  # dict_keys(['brand', 'model', 'year', 'color'])

c = mycar.values()
print(c)  # dict_values(['Range Rover Sports', 'HSE', 2022, 'silver'])

mycar.pop("color")
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2022}

del mycar["model"]
print(mycar)  # {'brand': 'Range Rover Sports', 'year': 2022}

mycar.clear()  # {}
print(mycar)

del mycar
print(mycar)  # Traceback (most recent call last):
            # File "/home/carl/Desktop/MatsHub/Python-CompLearn/my_notes/python_data_ structures/built_in_dictionary_methods.py", line 59, in <module>
            #     print(mycar)
            # NameError: name 'mycar' is not defined
