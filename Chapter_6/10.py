from random import *
def approxPi(dart):
    k = 0
    for i in range(dart):
        x = uniform(0, 2)
        y = uniform(0, 2)
        if (x-1)**2 + (y-1)**2 <= 1:
            k += 1

    return 4 * k / dart

print(approxPi(1000))
print(approxPi(100000))
print(approxPi(1000000))