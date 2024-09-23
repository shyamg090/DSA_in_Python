def small(l,n):

    res = []

    for i in l:
        if i < n:
            res.append(i)

    return res

print(small([9,100, 20, 40, 3, 7],10))