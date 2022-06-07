'''             POLYMORPHISM  PART 3








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
        
def europe(eu):
    eu.capital_city()


# ******************************************
queen = UK()
# queen.capital_city()

zara = Spain()
# zara.capital_city()
europe(queen)
europe(zara)

'''
for country in (queen,zara):
    country.capital_city()
    country.language()
'''
# Londin is the capital of UK
# Madrid is the capital of Spain
# Londin is the capital of UK
# English is the primary language 
# Madrid is the capital of Spain
# Spanish is the primary language 

#  Create Polymorphism by using existing method on new function.

# Londin is the capital of UK
# Madrid is the capital of Spain

