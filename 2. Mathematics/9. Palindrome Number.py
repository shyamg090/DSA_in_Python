class Solution:
    def isPalindrome(self, x: int) -> bool:
        if( x < 0):
            return False

        rev = 0
        temp = x
        while temp != 0:
            ld = temp % 10
            rev = rev * 10 + ld
            temp = temp // 10

        if rev == x:
            return True 
        else:
            return False
            
            