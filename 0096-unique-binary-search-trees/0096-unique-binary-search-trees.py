class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1  # empty tree: 1 way
        dp[1] = 1 if n >= 1 else 0

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left_count = dp[root - 1]
                right_count = dp[nodes - root]
                total += left_count * right_count
            dp[nodes] = total

        return dp[n]