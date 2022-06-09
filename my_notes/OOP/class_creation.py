'''             CREATING A CLASS
'
Created with the keyword 'CLASS' FOLLOWED BY A NAME.
Common practice is to make the names Pascal Casing: Example: MyFirstCar
A class consists of variables (Attributes) and functions (Methods)
Class can be used to model  a lot of things in the real world.

__init__() is a built-in function in Python. Also knowen as the initializer. used to initialize objects with initial values. All classes should have them. It is called automatically when a new object is created from a class.

self parameter is a reference to the current instance of the class. It is the first parameter of any method(function) in a class. It is used to access variables and methods belonging to the class. Also used to add attributes to a method.









'''
class Instructures:
    companyName = "Bluelime"

    def __init__(self,course):
        self.course = course

    def printinfo(self):
        print("My Company name is ", Instructures.companyName)

class Pets:
    pass