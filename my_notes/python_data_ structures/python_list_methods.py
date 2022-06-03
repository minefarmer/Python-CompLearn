'''              extend() method  line 31
Used to append or join list contents.

                 sort() method line 50
Sort method is basically used to order the items in the list in either dascending or ascending order. (ascending is default, A to Z, to change specify == reverse)

                count() method line 60
Counts the occurrence of a list item or element in a list.

                index() method line 90
The index method is used to return the index position of a specific item.

                pop() method  line 120
The pop method is used to remove the last item on the list, when nothing is specified in the list.
I can specify what to remove as a parameter.

                remove() method line 150
Removes the specified item from a list.

                del() method line 180
It is basically used to delete an item from the list if i pas in the index in between the parenthesis.
                
                
                
                
                
                
                
                
'''
# fruits = ["berries", "apples", "grapes", "oranges"]
# vegetables = ["kale", "broccoli", "lettace"]

# fruits.extend(vegetables)
# print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# vegetables.append("bean")
# print(vegetables)  # ['kale', 'broccoli', 'lettace', 'bean']
# print(fruits)  # does not contain 'bean', because the extend wss done before I did the append on the vegetable list.  ## ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']










# sort()
# fruits = ["berries", "apples", "grapes", "oranges"]
# vegetables = ["kale", "broccoli", "lettace"]

# fruits.extend(vegetables)
# print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# vegetables.append("bean")
# print(vegetables)  # ['kale', 'broccoli', 'lettace', 'bean']

# vegetables.sort()
# print(vegetables) # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace'# ['kale', 'broccoli', 'lettace', 'bean'] # ['bean', 'broccoli', 'kale', 'lettace'

# vegetables.sort(reverse=True)
# print(vegetables) # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']
                # ['kale', 'broccoli', 'lettace', 'bean']
                # ['bean', 'broccoli', 'kale', 'lettace']
                # ['lettace', 'kale', 'broccoli', 'bean']


# count()
# fruits = ["berries", "apples", "grapes", "oranges"]
# vegetables = ["kale", "broccoli", "lettace"]

# fruits.extend(vegetables)
# print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# vegetables.append("bean")
# print(vegetables)  # ['kale', 'broccoli', 'lettace', 'bean']

# vegetables.sort()
# print(vegetables) # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace'# ['kale', 'broccoli', 'lettace', 'bean'] # ['bean', 'broccoli', 'kale', 'lettace'

# vegetables.sort(reverse=True)
# print(vegetables)

# print(fruits.count("berries")) # ['1']



#  index()
# fruits = ["berries", "apples", "grapes", "oranges"]
# vegetables = ["kale", "broccoli", "lettace"]

# fruits.extend(vegetables)
# # print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# vegetables.append("bean")
# # print(vegetables)  # ['kale', 'broccoli', 'lettace', 'bean']

# vegetables.sort()
# # print(vegetables) # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace'# ['kale', 'broccoli', 'lettace', 'bean'] # ['bean', 'broccoli', 'kale', 'lettace'

# vegetables.sort(reverse=True)
# print(vegetables)  # ['lettace', 'kale', 'broccoli', 'bean']

# print(fruits.count("berries")) # 1

# print(fruits.index("grapes"))  # 2

# fruits.insert(0, "banana") #
# print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']








# pop() method
# fruits = ["berries", "apples", "grapes", "oranges"]
# vegetables = ["kale", "broccoli", "lettace"]

# fruits.extend(vegetables)
# # print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# vegetables.append("bean")
# # print(vegetables)  # ['kale', 'broccoli', 'lettace', 'bean']

# vegetables.sort()
# # print(vegetables) # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace'# ['kale', 'broccoli', 'lettace', 'bean'] # ['bean', 'broccoli', 'kale', 'lettace'

# vegetables.sort(reverse=True)
# print(vegetables)  # ['lettace', 'kale', 'broccoli', 'bean']

# print(fruits.count("berries")) # 1

# print(fruits.index("grapes"))  # 2

# fruits.insert(0, "banana") #
# print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# fruits.pop()
# print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli']





# remove()
# fruits = ["berries", "apples", "grapes", "oranges"]
# vegetables = ["kale", "broccoli", "lettace"]

# fruits.extend(vegetables)
# # print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# vegetables.append("bean")
# # print(vegetables)  # ['kale', 'broccoli', 'lettace', 'bean']

# vegetables.sort()
# # print(vegetables) # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace'# ['kale', 'broccoli', 'lettace', 'bean'] # ['bean', 'broccoli', 'kale', 'lettace'

# vegetables.sort(reverse=True)
# print(vegetables)  # ['lettace', 'kale', 'broccoli', 'bean']

# print(fruits.count("berries")) # 1

# print(fruits.index("grapes"))  # 2

# fruits.insert(0, "banana") #
# print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

# fruits.pop()
# print(fruits)

# vegetables.remove("kale")
# print(vegetables)  # ['lettace', 'broccoli', 'bean']


# del() method
fruits = ["berries", "apples", "grapes", "oranges"]
vegetables = ["kale", "broccoli", "lettace"]

fruits.extend(vegetables)
# print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

vegetables.append("bean")
# print(vegetables)  # ['kale', 'broccoli', 'lettace', 'bean']

vegetables.sort()
# print(vegetables) # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace'# ['kale', 'broccoli', 'lettace', 'bean'] # ['bean', 'broccoli', 'kale', 'lettace'

vegetables.sort(reverse=True)
print(vegetables)  # ['lettace', 'kale', 'broccoli', 'bean']

print(fruits.count("berries")) # 1

print(fruits.index("grapes"))  # 2

fruits.insert(0, "banana") #
print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettace']

fruits.pop()
print(fruits)

vegetables.remove("kale")
print(vegetables)  # ['lettace', 'broccoli', 'bean']

del vegetables
print(vegetables) # Traceback (most recent call last):
                # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\python_data_ structures\python_list_methods.py", line 210, in <module>
                #     print(vegetables) # ['lettace']
                # NameError: name 'vegetables' is not defined
