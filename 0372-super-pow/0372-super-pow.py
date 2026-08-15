class Solution(object):
    def superPow(self, a, b):
        MOD = 1337

        def modpow(base, exp, mod):
            base %= mod
            result = 1
            while exp > 0:
                if exp & 1:
                    result = result * base % mod
                base = base * base % mod
                exp >>= 1
            return result

        result = 1
        for digit in b:
            result = modpow(result, 10, MOD) * modpow(a, digit, MOD) % MOD
        return result