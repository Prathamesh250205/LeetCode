class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
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

        max_val = pow(2, p, MOD)       
        biggest = (max_val - 1) % MOD     
        pair_val = (max_val - 2) % MOD   
        num_pairs = fastPow(2, p - 1, MOD) - 1 if p > 0 else 0 
        num_pairs = (1 << (p - 1)) - 1

        result = (biggest * fastPow(pair_val, num_pairs, MOD)) % MOD
        return result