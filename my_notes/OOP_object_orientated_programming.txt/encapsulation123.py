'''             WHAT IS ENCAPSULATION  Part 1, 2

Process of restricting access to methops and variables to prevent direct data modification.

Public methods and variables are accessable from anywhere in the program.

Private methods and variables are accessible from thier own class.

Double underscore prefix before object name makes it private.
'''
class Cars:
    def __init__(self,speed,color):
        self.__speed = speed    # the double underscore makes the spped private
        self.__color = color    #  dito

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

ford = Cars(250,"green")
nissan = Cars(300, "red")
toyota = Cars(350, "blue")

ford.set_speed(450)  # this set a new speed for the ford on line 22. = because there is noencapsulation

ford.speed = 500   # this set a new speed for the ford on line 22. = because there is noencapsulation

print(ford.get_speed())  # 500

# print(ford.__color)  # greenTraceback (most recent call last):
                    # File "/home/carl/Desktop/MatsHub/Python-CompLearn/my_notes/OOP_object_orientated_programming.txt/encapsulation123.py", line 32, in <module>
                    #     print(ford.__color)  # green
                    # AttributeError: 'Cars' object has no attribute '__color'
