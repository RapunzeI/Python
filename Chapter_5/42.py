def primeFac(n):
    primeList=[]
    for i in range(2, n+1):
        bData=True #소수임
        for k in range(2, i):
            if i%k==0:
                bData=False #소수가 아님
                break
        if bData:
            while(n%i==0):
                primeList.append(i)
                n=n/i
    return primeList

print(primeFac(5))
print(primeFac(72))