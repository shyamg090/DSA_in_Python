def power(x,n):
    if(n == 0):
        return 1
    
    if(n % 2 == 0):
        return power(x, n/2) * power(x, n/2)
    else:
        return power(x, n-1) * x

print(power(5,5))