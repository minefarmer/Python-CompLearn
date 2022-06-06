'''             WHAT ARE DECORATORS? 
Decorators are used to add new functionality to existing objects like functions, methods and classes without modifying it's structure.

Decorators are usually called before the defination of the object (Function, Method, Class) we want to decorate.

They can be represented by @ followed by the name of the decorated object.

        Creating a Decorator
Convert a sentance to uppercase.
I'm going to achieve this by defining a wrapper inside an enclosed finction.


For more info:
    https;//WWW.PYTHON.ORG/DEV/PEPS/PEP-0318/






'''
def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper
@my_decorator
def say_hello():
    return "hello world"
# decorate = my_decorator(say_hello)
print(say_hello())  # HELLO WORLD
# print(decorate())  # HELLO WORLD
