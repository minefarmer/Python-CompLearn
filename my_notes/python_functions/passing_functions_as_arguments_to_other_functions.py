'''             PASSING FUNCTIONS AS ARGUMENTS TO OTHER FUNCTIONS








'''
def mynum(b):
    return b + 1
def addnum(c):
    newnum = 7
    return c(newnum)
print(addnum(mynum))  # 8

