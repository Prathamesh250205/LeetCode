class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def fastPow(base, exp):
            if exp == 0:
                return 1.0
            half = fastPow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            x = 1 / x
            n = -n

        return fastPow(x, n)