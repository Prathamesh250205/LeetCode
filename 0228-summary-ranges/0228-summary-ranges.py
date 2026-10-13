class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(nums)
        
        while i < n:
            start = nums[i]
            
            # Extend the range as long as consecutive elements differ by 1
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
                
            end = nums[i]
            
            # Format and add to result
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))
                
            i += 1
            
        return result