class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        low, high = min(nums), max(nums)
        present = set(nums)
        
        result = []
        for val in range(low, high + 1):
            if val not in present:
                result.append(val)
        
        return result