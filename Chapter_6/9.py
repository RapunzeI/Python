from random import *

def guess(max):
    num = randrange(0, max)
    while True:
        userGuess = eval(input('Enter your guess: '))

        if num == userGuess:
            print('You got it!')
            break
        elif num < userGuess:
            print('Too high.')
        elif num > userGuess:
            print('Too low.')

guess(100)