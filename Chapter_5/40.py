def approxPi(error):
    prev=4/1-4/3
    curr=prev+4/5-4/7
    i=5
    while curr-prev>error:
        prev=curr
        curr+=4/(2*i-1)-4/(2*i+1)
        i+=2
    return curr

print(approxPi(0.01))
print(approxPi(0.0000001))