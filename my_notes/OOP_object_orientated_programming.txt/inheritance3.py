'''              WHAT IS INHERITANCE   Part 1

inHeritance is basically the process that allows us to create a new class and reusing the code from an existing parent class.

The parent class (superclass or base class) is the class being inherited from.

The child class (subclass or dirived) is the class that inherits from another class.


'''
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

florist = Person("Jane", "Flowers")
florist.printname()  # Jane Flowers 




'''                 WHAT IS INHERITANCE   Part 3  **********************************

    Creating a child class.

        __init__()  # to be added to our child class.

When we add a child class without an (__init__()) method, it inherits all the methods and attributes of the parent class.

If I give the child class it's own (__init__())  method, it will over ride the init meth of the parent class.


'''





class Lawyers(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        # self.firstname = fname
        # self.lastname = lname
    
    def printinfo(self):
        print(self.firstname, self.lastname)



happy_lawyers = Lawyers("Jack", "Smiley")
happy_lawyers.printinfo()   # Jane Flowers
                            # Jack Smiley




