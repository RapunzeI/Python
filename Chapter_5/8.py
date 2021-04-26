def bubblesort(lst):
    for i in range(1,len(lst)):
        for k in range(len(lst)-i):
            if lst[k]>lst[k+1]:
                tmp=lst[k]
                lst[k]=lst[k+1]
                lst[k+1]=tmp
    return lst

lst = [3,1,7,9,2,5]
bubblesort(lst)
print(lst)