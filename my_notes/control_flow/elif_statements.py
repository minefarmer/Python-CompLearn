'''             WHAT ARE ELIF STATEMENTS?

Kind of a combination of a else statement and a if statement.
They are used to check for multiple expressions that are true or false.
It executes the first one it finds and then ignores the rest.
It then executes that block of code inside the if block, and if the condition is not True, it doesn't do anything.

if(condition1):
    Indented statement block for Condition1
elif(condition2):       # I can have as many elif statements as I want.
    Indented statement block for Condition2

'''
a = 7
b = 8

if a > b:  # > an operator
    print(a, " is smaller than ", b)  # nothing is printed
    
elif b > a: # > an operator
    print(b, " is bigger than", a)   # 8  is bigger than 7

