class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]:
                # Climbing up towards the right; peak must be on the right
                left = mid + 1
            else:
                # Descending; peak is at mid or on the left
                right = mid
                
        return left