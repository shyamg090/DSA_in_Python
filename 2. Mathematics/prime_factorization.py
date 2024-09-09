def isPrime(x):
    if x == 2 or x == 3:
        return True
    
    if x % 2 ==0 or x % 3 == 0:
        return False

    i = 5
    while i * i <= x:

        if x % i == 0 or x % (i+2) == 0:
            return False
        
        i = i + 6

    return True

def number(n):
    a = n
    i = 2
    ans = []
    for i in range (2 , n):

        if ( isPrime(i) ):
            x = i
            while n % x == 0:
                print(i)
                x = x * i
        i = i + 1
        # check if it is divisible 


print(number(120))


    
