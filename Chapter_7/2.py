def f(y):
    x = 2
    return g(x)
# f, g : 전역
# x, y : 지역

def g(y):
    global x
    x = 4
    return x * y
# g, x : 전역
# y : 지역

x = 0
res = f(x)
print('x = {}, f(0) = {}'.format(x, res))
# x, res, f : 전역
