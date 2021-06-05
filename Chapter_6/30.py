from random import *
def simul(n):
    p1_win = 0
    p2_win = 0

    # 가위 : 0, 바위 : 1, 보 : 2
    for i in range(n):
        p1 = randint(0, 2)
        p2 = randint(0, 2)

        if p1 == 0:
            if p2 == 1:
                p2_win += 1
            elif p2 == 2:
                p1_win += 1
        elif p1 == 1:
            if p2 == 0:
                p1_win += 1
            elif p2 == 2:
                p2_win += 1
        elif p1 == 2:
            if p2 == 1:
                p1_win += 1
            elif p2 == 0:
                p2_win += 1
    
    if p1_win > p2_win:
        return 'Player 1'
    elif p1_win < p2_win:
        return 'Player 2'
    else:
        return 'Tie'

print(simul(1))
print(simul(1))
print(simul(10000))