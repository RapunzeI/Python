def interest(interestRate):
    yearCnt=1
    Rate=interestRate
    while Rate<1:
        Rate+=interestRate + interestRate*Rate
        yearCnt+=1

    return yearCnt

print(interest(0.07))
print(interest(0.1))