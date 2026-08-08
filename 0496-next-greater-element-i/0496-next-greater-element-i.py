class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                next_greater[stack.pop()] = n
            stack.append(n)
        return [next_greater.get(n, -1) for n in nums1]