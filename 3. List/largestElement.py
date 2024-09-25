def largest(l):
    if not l:
        return None
    
    max = 0 
    for i in l:
        if(max <= i):
            max = i
    return max

print(largest([10,20,5,50]))