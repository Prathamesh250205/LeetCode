class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if nums[i] == target else -1)

 
        offset = n + 2
        size = 2 * n + 4
        tree = [0] * (size + 1)

        def update(i):
            while i <= size:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        result = 0
        for val in prefix:
            idx = val + offset
            result += query(idx - 1) 
            update(idx)

        return result