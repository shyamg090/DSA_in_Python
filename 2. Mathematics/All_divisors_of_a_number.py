# naive approach
def divisors(n):
    for i in range (1,n+1):
        if n % i == 0:
            print(i)
        i+=1
#
# Eficient approach 
def divisors2(n):
    i = 1
    while (i * i <= n):
        if n % i == 0:
            print(i)
            if i != n//i:
                print(n//i) 
        i+=1

# Optimal Approach
def divisors3(n):
    i = 1
    while( i * i < n ):
        if( n % i == 0 ):
            print(i)
        i += 1
    
    while( i >= 1):
        if( n % i == 0):
            print( n//i )
        i -= 1
    
divisors(15)
print('hello there')
divisors2(15)
print('hello there')
divisors3(15)