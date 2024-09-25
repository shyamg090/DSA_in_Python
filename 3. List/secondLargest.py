def secLar(l):
    prev = 0
    maxi = 0
    count = 1
    # two pointer approach
    for i in l:
        if maxi < i:
            prev = maxi
            maxi = i
        elif maxi == i:
            count+=1
        elif i > prev:
            prev = i
    
    if count == len(l):
        return None

    return prev

print(secLar([10,20,100,91,95,101,200,55,5,50]))
print('$$$$$$$')
print(secLar([10,10,10,10,1]))
print('$$$$$$$')
print(secLar([10,10,10,10]))