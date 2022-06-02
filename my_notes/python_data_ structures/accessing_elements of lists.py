'''                ACCESSING ELEMENTS OF LISTS
Can be accessed using thier index or position in a list.
The index is zero based. First element has a position of zero.






'''
animals = ["bear", "tiger", "lion", "panda", "elephant"]
# for x in animals:
    # print(x)
# print(animals)
print(animals[0])  # bear
print(animals[-1]) # elephant
print(animals[1:])  # ['tiger', 'lion', 'panda', 'elephant']
print(animals[1:3])  # ['tiger', 'lion']
animals[0] = "dog"
print(animals[0]) # dog
