from math import *
def approxE(error):
    before=1
    after=2
    i=2
    while after-before>=error:
        before=after
        after=before+1/factorial(i)
        i+=1

    return after

print(approxE(0.01))
print(approxE(0.000000001))