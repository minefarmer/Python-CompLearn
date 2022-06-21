'''             NUMBER GUESSING GAME








'''
import random

guesses = []

myComputer = random.randint(1, 70)

player = int(input('Enter a number between 1-70: '))
guesses.append(player)

while player != myComputer:
    if player > myComputer:
        print('Number is too high!')
    else:
        print('Number is too low!')
    player = int(input('Enter a number between 1-70: '))
    guesses.append(player)
    
    
else:
    print(' You have quessed right! Good job!')
    print('It took you %i guesses. ' % len(guesses))
    print('These were your guesses: ')
    print(guesses)   
        # Number is too low!
        # Enter a number between 1-70: 60
        # Number is too high!
        # Enter a number between 1-70: 50
        # Number is too low!
        # Enter a number between 1-70: 55
        # You have quessed right! Good job!It took you 4 guesses.
        # These were your guesses:
        # [45, 60, 50, 55]