def h(n):
    print('Start h')
    try:
        print(1 / n)
    except:
        print('Caught!')
    print(n)

def g(n):
    try:
        print('Start g')
        try:
            h(n - 1)
        except:
            print('Caught!')
        print(n)
    except:
        print('Caught!')

def f(n):
    print('Start f')
    g(n - 1)
    print(n)

f(2)
# h() 에서 1 / n 은 1을 0으로 나누게 되므로, ZeroDivisionError 발생