class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1
        
        num_set = set(nums)
        while total in num_set:
            total += 1
        
        return total