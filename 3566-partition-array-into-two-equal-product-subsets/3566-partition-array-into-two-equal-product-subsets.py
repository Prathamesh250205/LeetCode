class Solution(object):
    def checkEqualPartitions(self, nums, target):
        n = len(nums)
        total = 1
        for x in nums:
            total *= x
        if total != target * target:
            return False

        def dfs(i, count, prod):
            if prod > target:
                return False
            if i == n:
                return count > 0 and count < n and prod == target
            if dfs(i + 1, count + 1, prod * nums[i]):
                return True
            return dfs(i + 1, count, prod)

        return dfs(0, 0, 1)