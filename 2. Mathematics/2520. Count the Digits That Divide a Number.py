class Solution:
    def countDigits(self, num: int) -> int:

        if num < 9:
            return 1

        count = 0
        d_num = num
        while d_num != 0:
            m = d_num % 10

            if num % m  == 0 :
                count = count + 1
            
            d_num = d_num // 10
        return count

        