def collatz(x):
    while x!=1:
        print(int(x))
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
    print(int(x))
collatz(10)