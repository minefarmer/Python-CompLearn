'''             WHAT ARE ELSE STATEMENTS?
Code that executes if conditions checked evaluate to False.

    SYNTAX FOR ELSE STATEMENTS
if(condition1):
    Indented statement block for Condition1
elif(condition2):
    Indented statement block for Condition2
else:
    Alternate statement block if all condition check above fails


'''
a = 7
b = 8
c = 9

if a > b:
    print(a, " is smaller than", b)
    
elif b >= c:
    print(b, " is smaller than", c)

else:
    print(c, "is larger than", b, "and", a)  # 9 is larger than 8 and 7
