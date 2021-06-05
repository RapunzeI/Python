from random import *
def game(n):
    cnt = 0
    for i in range(n):
        a = randint(0, 9)
        b = randint(0, 9)

        print(a, '+', b, '=')
        answer = eval(input('Enter answer: '))
        if answer == a + b:
            print('Correct.')
            cnt += 1
        else:
            print('Incorrect.')

    print('You got {} correct answers out of {}'.format(cnt, n))

game(10)