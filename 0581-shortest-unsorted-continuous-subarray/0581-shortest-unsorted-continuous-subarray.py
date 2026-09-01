class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        left, right = -1, -2
        max_val = nums[0]
        min_val = nums[-1]
        
        for i in range(1, n):
            max_val = max(max_val, nums[i])
            if nums[i] < max_val:
                right = i
                
            min_val = min(min_val, nums[n - 1 - i])
            if nums[n - 1 - i] > min_val:
                left = n - 1 - i
                
        return right - left + 1