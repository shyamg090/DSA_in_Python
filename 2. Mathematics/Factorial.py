# iterative with class
class Solution:
    def factorial (self, N):
        n = N
        res = 1
        
        for i in range ( 2, n+1 ):
           res = res * i
           
        return res

# recuresive with class
class Solution2:
    def factorial1 (self, N):
        if N == 0:
            return 1
        return N * self.factorial1 ( self, N - 1 )


# recursive without class
def factorial2 (self, N):
        if N == 0:
            return 1
        return N * factorial2 ( self, N - 1 )

