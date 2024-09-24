def small(l,n):

    res = []

    for i in l:
        if i < n:
            res.append(i)

    return res

# list comprehension\

def small2(l,num):
    return [ i for i in l if i < num ]


print(small2([9,100, 20, 40, 3, 7],10))

print('!!!!!!!!!!!!!!!!!!')

print(small([9,100, 20, 40, 3, 7],10))