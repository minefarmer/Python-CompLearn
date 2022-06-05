'''             FOR LOOP AND RANGE FUNCTION
range function is a built-in function of python.

The range()function generates the integer numbers between the given start int th the stop integer, which is generally used to iterate over with a for loop.

The range() function returns a sequence of numbers starting from zero by default. I can specify a start number.

When I have a range and I also need to increase the number I have specified in the range. For example, if I have a value of eight that I passed into my range, I wanted to generate a random number. What ot will do, it will increase it by one each time umtill it gets to that number I specified, by default. It increases by one, but I can change that and specify a number I want to do the increment by. Default increment is by one but I can change that and specify a number I want to do the increment by.

'''
# for x in range(8):
#     print(x)  # 0
            # 1
            # 2
            # 3
            # 4
            # 5
            # 6
            # 7

# for x in range(2,8):
#     print(x)  # 2
            # 3
            # 4
            # 5
            # 6
            # 7

for x in range(2,40,4):
    print(x)  # 2
6
10
14
18
22
26
30
34
38
