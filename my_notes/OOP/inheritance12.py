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




'''                 WHAT IS INHERITANCE   Part 2-3  **********************************

    Creating a child class.



'''
class Lawyers(Person):
    
happy_lawyers = Lawyers("Jack", "Smiley")
happy_lawyers.printname()   # Jane Flowers
                            # Jack Smiley



