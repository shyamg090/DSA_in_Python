# naive
def isPrime(i):
    if i == 2 or i == 3:
        return True
    if i % 2 == 0 or i % 3 == 0:
        return False
    x = 5
    while x*x <= i:
        if (i % x ==0 ) or ( i% x+2 == 0):
            return False
        i += 1
    return True

def sieve(n):
    if n == 1:
        print(n)
    if n == 2:
        print(n)
    i = 2
    while i != n:
        if(isPrime(i)):
            print(i)
        i += 1

# Better Approach
# def sieve2(n):
#         i = 2

#         isPrime2 = [True] * (n+1)

#         while i*i < n:
#             if isPrime2[i]:
#                 for j in range ( 2* i, n+1, i):
#                     isPrime2 = False
#             i += 1

#         for i in isPrime2:
#             if isPrime2[i]:
#                 print(i)

        


sieve(10)
print('-------')
# sieve2(10)