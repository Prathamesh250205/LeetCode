class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10 ** 9 + 7

        def power(base, exp, mod):
            result = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result

        even_count = (n + 1) // 2
        odd_count = n // 2

        return (power(5, even_count, MOD) * power(4, odd_count, MOD)) % MOD