'''             BUILT-IN SET METHODS
Method      Description
add()       Adds na element to a set.
Update()    Adds multiple elements to a set.
clear()     Removes all elements in a set.
discard()   Removes a specified element or item.
remove()    Removes a specified item from the set.
del()       Deletes the set.

'''
fruits = {"grapes","apples","berries"}
animals = (("lion","Tiger","bear"))
fruits.add("oranges")
print(fruits)  # {'berries', 'apples', 'oranges', 'grapes'}
fruits.update(["mango", 'kiwi'])
print(fruits)  # {'berries', 'mango', 'grapes', 'oranges', 'apples', 'kiwi'}
fruits.remove("kiwi")
print(fruits)  # {'mango', 'apples', 'grapes', 'berries', 'oranges'}
fruits.clear()
print(fruits)  # set()
del animals
print(animals)  # Traceback (most recent call last):
                # File "/home/carl/Desktop/MatsHub/Python-CompLearn/my_notes/python_data_ structures/built_in_set_methods.py", line 32, in <module>
                #     print(animals)
                # NameError: name 'animals' is not defined
