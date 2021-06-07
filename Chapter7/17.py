from random import *
def game(n):
    cnt = 0
    for i in range(n):
        a = randint(0, 9)
        b = randint(0, 9)

        print('{} + {} = '.format(a, b))
        while True:
            try:
                answer = eval(input('Enter answer: '))
                break
            except:
                print('Please write your answer using digits 0 though 9. Try again!')
        if answer == a + b:
            print('Correct.')
            cnt += 1
        else:
            print('Incorrect.')

    print('You got {} correct answers out of {}'.format(cnt, n))

game(3)