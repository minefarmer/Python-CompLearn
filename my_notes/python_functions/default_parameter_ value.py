'''             DEFAULT PARAMETER VALUE
This is the value a function uses when called without passingit a value.
Only parameters at the end of a parameter list can have a default value, as the values are assigned by the position
This is the proper way of assigning a default parameter value, because this has to parameters
'''
# def greeting(a,b=7)
'''
This is wrong!
def greeting(a=7,b)
'''
def student_names(names="Bluelime"):
    print("Hello " + names)


student_names()  # Hello Bluelime
student_names("Carl")  # Hello Carl
student_names("Rich")  # Hello Rich


