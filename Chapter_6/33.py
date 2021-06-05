from random import *
def diceprob(r):
    diceCnt = 0
    overHundred = 0
    while overHundred < 100:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        if dice1 + dice2 == r:
            overHundred += 1

        diceCnt += 1

    print('It took {} rolls to get 100 rolls of {}'.format(diceCnt, r))

diceprob(2)
diceprob(3)
diceprob(4)
diceprob(5)
diceprob(6)
diceprob(7)