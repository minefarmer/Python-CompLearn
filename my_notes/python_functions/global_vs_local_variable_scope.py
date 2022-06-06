'''             GLOBAL VS LOCAL VARIABLE SCOPE

Variables defined inside a function body have a local scope.
Variables defined outside a function have a global scope.
Global variable can be accessed from anywhere within my python file.
I can use the global keyword inside a function defination to make the value of a local variable global.



'''
# x = 10

# def my_numbers(x):
#     print(x)  # 10  # from line eleven.
#     x = 7
#     print("My fav number is ", x)  # My fav number is  7

# my_numbers(x)

# print(x)  # 10









# to change the original value of the global variable, I have to use the keyword (global) inside my function definition.
x = 10

def my_numbers():
    global x
    print(x)  # 10  # from line eleven.
    x = 7
    print("My fav number is ", x)  # My fav number is  7

my_numbers()

print(x)  # 7  ## The new global number from line 34
