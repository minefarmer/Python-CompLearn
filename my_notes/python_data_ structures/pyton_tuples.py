'''             WHAT IS A TUPLE?
            Creating a tuple with parenthesis  line 21
            Creating a tuple with a tuple constructor.  line 30

            
A tuple is a list that cannot be changed. (inmutable)
It can be created using parenthesis. () and with a constructor.
I can also use what is called a tuple constructor to create a tuple.
Once I've created a tuple, I can access the individual elements within a tuple by using the index.
Elements in a tuple can be accessed by thier index
Onced I have created a tuple, I can use a for loop to go thru the list and print it out on the screen.
Once I print a tuple, I cannot change, only delete.







'''
fruits = ("grapes", "apples", "berries")
for x in fruits:
    print(x)  # grapes, apples, berries
print(fruits[2])  # berries





# Creating a tuple with a tuple constructor.
animals = tuple(("lion","tiger","bear"))
# print(animals)  # ('lion', 'tiger', 'bear')
# print(len(animals))  # 3
# animals.add("dog")
# print(animals)  # Traceback (most recent call last):
                # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\python_data_ structures\pyton_tuples.py", line 34, in <module>
                #     animals.add("dog")
                # AttributeError: 'tuple' object has no attribute 'ad

# animals[0] = "cheetah"
# print(animals)  # Traceback (most recent call last):
                # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\python_data_ structures\pyton_tuples.py", line 39, in <module>
                #     animals[0] = "cheetah"
                # TypeError: 'tuple' object does not support item assignment

del animals
print(animals)  # Traceback (most recent call last):
  File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\python_data_ structures\pyton_tuples.py", line 47, in <module>
    print(animals)
NameError: name 'animals' is not defined
PS C:\Users\pgold\MatHub\Python-CompLearn>
