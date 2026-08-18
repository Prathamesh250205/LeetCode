from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        if k == n:
            return max(nums)
        if k == 1:
            cnt = Counter(nums)
            ans = -1
            for v, c in cnt.items():
                if c == 1:
                    ans = max(ans, v)
            return ans
        
        def windows_containing(val):
            count = 0
            freq = 0
            for i in range(n):
                if nums[i] == val:
                    freq += 1
                if i >= k and nums[i-k] == val:
                    freq -= 1
                if i >= k-1 and freq > 0:
                    count += 1
                    if count > 1:
                        return count
            return count
        
        ans = -1
        for val in (nums[0], nums[-1]):
            if windows_containing(val) == 1:
                ans = max(ans, val)
        return ans