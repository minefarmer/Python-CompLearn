'''             INSTANTIATING A CLASS

The process of creating an object from a class.

If I want to access the method of a class from an instance of the class, I could do that by typing in the object name and then I use the dot notation or the period followed by the name of the method.




'''
class Instructors:
    companyName = "Bluelime"

    def __init__(self,course):
        self.course = course

    def printinfo(self):
        print("My Company name is ", Instructors.companyName)
        
elearning = Instructors("Python for beginners")

bls = Instructors("Django for beginners")


'''     Accessing methods

If I want to access the method of a class from an instance of the class, I could do that by typing in the object name and then I use the dot notation or the period followed by the name of the method.






'''
bls.printinfo()  # My Company name is  Bluelime


'''     Accessing Attribute

ObjectName.Attribute

If I wanted to access an attribute that belonge to a class from an instance of the class, I can do so by using the object name, followed by a dot notation and then the name of the attribute.


'''
print(bls.course)  # Django for beginners

