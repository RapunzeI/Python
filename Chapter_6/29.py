def networks(student ,friend):
    groups = []
    zero = set()

    for i in range(len(friend)):
        for k in range(i + 1, len(friend)):
            if set(friend[i]) & set(friend[k]) != zero:
                groups.append(set(friend[i]) | set(friend[k]))
    alone = []
    for i in friend:
        for k in groups:
            if set(i) <= k:
                b = False
                break
        if b == True: alone.append(set(i))
        b = True


    index = 0
    groups += alone
    for i in groups:
        print('Social network {} is {}'.format(index, i))
        index += 1

networks(6, [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)])