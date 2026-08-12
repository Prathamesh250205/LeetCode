class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        best = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best