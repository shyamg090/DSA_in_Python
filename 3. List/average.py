def average(l):
    n = len(l)
    sum = 0 

    for i in l:
        sum = sum + i
    
    return sum / n

# or 

def average2(l):    
    return sum(l) / len(l)

print(average([30,60,40]))
print('######################')
print(average2([30,60,40]))