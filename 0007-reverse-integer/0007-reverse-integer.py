class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        result = 0
        while x != 0:
            digit = x % 10
            x //= 10
            result = result * 10 + digit
        
        result *= sign
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result