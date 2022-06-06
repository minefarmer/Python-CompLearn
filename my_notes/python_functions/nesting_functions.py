'''             NESTING FUNCTIONS








'''
def mynum(a):
    def num(a):
        return a + 1
    result = num(a)
    return result
print(mynum(4))  # 5  ##  4 plus line 13

