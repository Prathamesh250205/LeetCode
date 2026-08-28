class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for c in costs:
            count[c] += 1

        bars = 0
        for price in range(1, max_cost + 1):
            if count[price] == 0:
                continue
            affordable = min(count[price], coins // price)
            bars += affordable
            coins -= affordable * price
            if coins == 0:
                break

        return bars