class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        # DP tables
        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]
        
        # Base cases: single elements
        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]
            
        # Prefix sum array for O(1) interval sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]
            
        # Bottom-up interval DP
        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Maintain two-pointer split boundary where left_sum <= total_sum / 2
                if mid < i:
                    mid = i
                while mid < j and (get_sum(i, mid) * 2) < get_sum(i, j):
                    mid += 1
                
                res = 0
                
                # Case 1: left_sum < right_sum -> Alice takes left side
                if mid > i:
                    res = max(res, maxL[i][mid - 1])
                
                # Case 2: left_sum == right_sum -> Alice takes either side
                if (get_sum(i, mid) * 2) == get_sum(i, j):
                    res = max(res, maxL[i][mid], maxR[mid + 1][j])
                    # Case 3: right_sum < left_sum -> Alice takes right side
                    if mid + 2 <= j:
                        res = max(res, maxR[mid + 2][j])
                else:
                    # Case 3: right_sum < left_sum -> Alice takes right side
                    if mid + 1 <= j:
                        res = max(res, maxR[mid + 1][j])
                
                dp[i][j] = res
                
                total = get_sum(i, j)
                maxL[i][j] = max(maxL[i][j - 1], res + total)
                maxR[i][j] = max(maxR[i + 1][j], res + total)
                
        return dp[0][n - 1]