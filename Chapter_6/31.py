from random import *

def craps():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)

    sum = dice1 + dice2
    if sum == 7 or sum == 11:
        return 1
    elif sum == 2 or sum == 3 or sum == 12:
        return 0
    else:
        while True:
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            sum2 = dice1 + dice2
            if sum2 == sum:
                return 1
            elif sum2 == 7:
                return 0

print(craps())
print(craps())
print(craps())