'''                 LOTTERY NUMBERS SIMULATOR
Importing Random Module.
Creating a list.
For loop and While loop.
Randint function.
List functions - append and sort
Print function
Range function

'''
import random

lottery_numbers = []

for i in range(0,6):
    number = random.randint(1,50)
    while number in lottery_numbers:
        number = number.randint(1,50)

    lottery_numbers.append(number)

lottery_numbers.sort()

print(lottery_numbers)  # [16, 18, 19, 45, 47, 48]
                        # [19, 22, 24, 34, 35, 43]

