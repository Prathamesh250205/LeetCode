class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        p = 1
        for ch in str(n):
            d = int(ch)
            s += d
            p *= d
        return n % (s + p) == 0