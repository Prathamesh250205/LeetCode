class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        count = [0] * (max_val + 1)
        for x in nums:
            count[x] += 1


        prefix = 0
        for v in range(max_val + 1):
            current = count[v]
            count[v] = prefix
            prefix += current

        return [count[x] for x in nums]