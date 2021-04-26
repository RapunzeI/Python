def sublist(list1, list2):
    index=0
    lst=[]
    for i in range(len(list1)):
        for j in range(index, len(list2)):
            if list1[i]==list2[j]:
                index=j
                lst.append(list1[i])
                break
    if lst==list1:
        return True
    else:
        return False

        

print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))

