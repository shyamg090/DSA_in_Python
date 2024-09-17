class Solution:
    #You need to complete this function
    def factorial(self,N):
        if (N == 0) or (N ==1):
            return 1
            
        return N * self.factorial(N - 1 )