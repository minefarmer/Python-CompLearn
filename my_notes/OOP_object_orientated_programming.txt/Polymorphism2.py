'''             POLYMORPHISM  PART 2  








'''
def addNumbers(a,b,c=1):
    return a + b + c

print(addNumbers(8,9))  # 18           # What I'm doing here is passing arguments for the function parameters.

print(addNumbers(8,9,4))  # 21

class UK():     # Polymorphic class with methods
    def capital_city(self):
        print("Londin is the capital of UK")

    def language(self):
        print("English is the primary language ")


class Spain():     # Polymorphic class with methods
    def capital_city(self):
        print("Madrid is the capital of Spain")

    def language(self):
        print("Spanish is the primary language ")
        
        