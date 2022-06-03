'''             WHAT IS A PYTHON SET?
            How to create a set with a constructer.   line 20
            Counting values in a Set.                 line 35
        
A set is a collection of values.
Values in a set are not ordered. They are not in any particular order and the values in the set are not indexted.
I can add values to a set, but, I cannot change values.

            How to create a Set
Try to give it a discriptive name that reflects the type of values it stores and then I add curly braces. {}

'''
fruits = {"grapes","apples","berries"}
for x in fruits:
    print(x)  # grapes
            # berries
            # apples
            
            
'''        How to create a set with a constructor()
animals = set(("lion","tiger","bear"))

animals = (("lion","tiger","bear"))
# If I do not add the keyword set to the constructor. It will create a tuple data type.
# When using the constructoe function, notice I have double parentheses.
'''
animals = (("lion","tiger","bear"))
for x in animals:
    print(x)   # lion
            # tiger
            # bear
print(len(animals))  # 3


''' Counting values in a Set.
 I can use the len() function.
'''
print(len(fruits))  # 3

