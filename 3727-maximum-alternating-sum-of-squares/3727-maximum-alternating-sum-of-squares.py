class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert each number to its square and sort in descending order
        squared = sorted([x * x for x in nums], reverse=True)
        
        n = len(nums)
        pos_count = (n + 1) // 2
        
        # Add the largest pos_count elements, subtract the rest
        return sum(squared[:pos_count]) - sum(squared[pos_count:])