def prime(a):
    if a == 1:
        return False
    
    for i in range (2, a):
        if a % 2 == 0:
            return False
        
    return True

def optimal_prime(a):
    if a == 1:
        return False
    
    i=2
    
    while ( i*i <= n):

        if(n % i == 0):
            return False

        i+=1
    
    return True
    
print(prime(11))
print("     ")
print(prime(13))
print("     ")
print(prime(14))
print("     ")
print(prime(2))
print("-------------------")
print(optimal_prime(11))
print("     ")
print(optimal_prime(13))
print("     ")
print(optimal_prime(14))
print("     ")
print(optimal_prime(2))