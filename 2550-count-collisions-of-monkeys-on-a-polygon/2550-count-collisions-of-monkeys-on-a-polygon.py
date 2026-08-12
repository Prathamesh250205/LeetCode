class Solution(object):
    def monkeyMove(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def fastPow(base, exp, mod):
            if exp == 0:
                return 1
            half = fastPow(base, exp // 2, mod)
            result = (half * half) % mod
            if exp % 2 == 1:
                result = (result * base) % mod
            return result

        total = fastPow(2, n, MOD)
        return (total - 2) % MOD