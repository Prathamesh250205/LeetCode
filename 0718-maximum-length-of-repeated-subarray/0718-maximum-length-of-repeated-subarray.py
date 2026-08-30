class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        best = 0

        for i in range(1, m + 1):
            prev = 0 
            for j in range(1, n + 1):
                temp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                    best = max(best, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return best