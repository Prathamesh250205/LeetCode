class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digitProduct(num):
            product = 1
            for char in str(num):
                product *= int(char)
            return product
        
        num = n
        while digitProduct(num) % t != 0:
            num += 1
        
        return num