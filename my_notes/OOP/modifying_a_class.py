'''             MODIFYING A CLASS

Add new attributes.
Modify existing attribute values.
Delete attributes.




'''
class Instructors:
    companyName = "Bluelime"

    def __init__(self,course,duration):
        self.course = course
        self.duration = duration

    def printinfo(self):
        print("My Company name is ", Instructors.companyName)
        
elearning = Instructors("Python for beginners",7)

bls = Instructors("Django for beginners",8)

bls.course = "HTML"

bls.printinfo()  # My Company name is  Bluelime

print(bls.course)  # HTML 

print(bls.duration)  # 8

del bls.duration  #

print(bls.course)  # HTML




'''             IMPORTING CLASSES

They can be imported into other classes like python modules


'''