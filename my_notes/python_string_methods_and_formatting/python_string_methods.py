'''         PYTHON STRING METHODS   PART 1    line 11
                                    PART 2    line 50







'''
# len()  # method
g ="hello world."

print(len(g))  # 12


# index()  # method
print(g.index("world"))  # 6


# capitalize()   ** Converts the first character to uppercase
print(g.capitalize())  # Hello world.


#  upper()  # Converts to uppercase.
print(g.upper()) # HELLO WORLD.


#  lower()  # Converts string to lowercase
print(g.lower())  # hello world.


# islower() # Checks for lower case. Works on the results of line 30
print(g.islower())  # True

# isupper() # Checks for lower case. Works on the results of line 30nb
print(g.isupper()) # False












# Part 2 ************************************************************************
# find()  # used to find the first index occurrence of a string or character.
print(g.find("world"))

# count()  # this method is used to count the occurrence of a string or character, so it will count how many times a particular string or character appears.
print(g.count("l"))  # 3

#  split()  # Is basically used to split a python string into a python list.
print(g.split())  # ['hello', 'world.']

# new line
print("show me\n d money")  # show me
                            #  d money
                            
                            
#  Concatenation + ## Is use to add strings or characters together and is done by using the arithmetic operator code plus(+)
print(g + " Hope u r doing ok. ")  # hello world. Hope u r doing ok.


#  replace()  # replaces strings or characters within a string. It takes two parameters. What to replace and what with.
print(g.replace("world", "people"))  # hello people.

