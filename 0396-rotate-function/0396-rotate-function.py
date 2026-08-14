class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_f = f
        
        for k in range(1, n):
            f += total - n * nums[n - k]
            max_f = max(max_f, f)
        
        return max_f