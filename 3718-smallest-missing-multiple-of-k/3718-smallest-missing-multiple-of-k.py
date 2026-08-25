class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        present = set(nums)
        m = k
        while m in present:
            m += k
        return m