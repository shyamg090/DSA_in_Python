def isPrime(x):
        if x == 2 or x == 3:
            return True
        
        if x % 2 == 0 or x % 3 == 0:
            return False
        
        i = 5
        while i * i <= x:
            if( x % i == 0 ) or ( x % i + 2 == 0 ):
                return False
        i = i + 6
        return True

def distinctPrimeFactors(nums):
    prod = 1
    for i in nums:
        prod = prod * i
        
    count_set = set(())

    for i in range (2, prod):
        x = i
        if( isPrime(x) ):
            x = i
            while ( prod % x == 0):
                count_set.add(i)
        i = i + 1
        
    return len(count_set)

list = [2,4,3,7,10,6]
print(distinctPrimeFactors(list))