class Solution(object):
    def maxProduct(self, nums):
        result = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        
        for num in nums[1:]:
            candidates = (num, max_prod * num, min_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)
            result = max(result, max_prod)
        
        return result