class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(x):
            if x == 0:
                return 1
            return x * factorial(x - 1)

        digits = [str(i) for i in range(1, n + 1)]
        k -= 1  # convert to 0-indexed
        result = []

        def build(nums, k):
            if not nums:
                return
            m = len(nums)
            block_size = factorial(m - 1)
            index = k // block_size
            result.append(nums[index])
            remaining = nums[:index] + nums[index + 1:]
            build(remaining, k % block_size)

        build(digits, k)
        return ''.join(result)