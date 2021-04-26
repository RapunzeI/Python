def inversions(alpha):
    alpha=list(alpha)
    cnt=0
    for i in range(1,len(alpha)):
        for k in range(len(alpha)-i):
            if alpha[k]>alpha[k+1]:
                tmp=alpha[k]
                alpha[k]=alpha[k+1]
                alpha[k+1]=tmp
                cnt+=1
    return cnt

print(inversions('ABBFHDL'))
print(inversions('ABCD'))
print(inversions('DCBA'))
