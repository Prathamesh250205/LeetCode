from itertools import combinations

class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        n = len(coins)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def count_le(mid):
            total = 0
            for r in range(1, n + 1):
                for combo in combinations(coins, r):
                    lcm = combo[0]
                    for c in combo[1:]:
                        lcm = lcm * c // gcd(lcm, c)
                    if r % 2 == 1:
                        total += mid // lcm
                    else:
                        total -= mid // lcm
            return total

        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo