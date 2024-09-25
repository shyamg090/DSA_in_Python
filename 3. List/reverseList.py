def rev(l):
    s = 0
    e = len(l)

    if e == 0 or e == 1:
        return l
    
    while s != e:
        temp = l[s]
        l[s] = l[e-1]
        l[e-1] = temp

        s+=1
        e-=1

    return l

# inbuilt method
l =  [100,30,60,393,12,10]
l.reverse()
print(l)
print('##########')


print(rev([10,30,50,33,11,1]))
print('##########')
print(rev(["chad","giga","is","trump"]))
