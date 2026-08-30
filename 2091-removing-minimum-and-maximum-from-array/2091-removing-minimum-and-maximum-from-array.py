class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))

        if i > j:
            i, j = j, i


        from_front = j + 1
        from_back = n - i
        both_ends = (i + 1) + (n - j)

        return min(from_front, from_back, both_ends)