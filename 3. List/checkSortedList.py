def issorted(l):
    s = 0
    e = len(l)
    # print(e)
    if e == 0 or e == 1:
        return True

    while s != e:
        if l[s] > l[e-1]:
            return False
        s+=1
        e-=1

    return True

# inbuilt sort 
def issorted2(l):
    newSort = sorted(l)
    if newSort == l:
        return True
    else:
        return False

print(issorted([10,20,100,91,95,101,200,55,5,50]))
print('@@@@@@@@@@@@@@@@@@')
print(issorted([10,20,30,41,55,61]))
print('@@@@@@@@@@@@@@@@@@')
print(issorted([]))
print('@@@@@@@@@@@@@@@@@@')
print(issorted([10,20,20,20,20,30,30,40]))
print('@@@@@@@@@@@@@@@@@@ - issorted2')
print(issorted([10,20,20,20,11,20,30,30,40]))