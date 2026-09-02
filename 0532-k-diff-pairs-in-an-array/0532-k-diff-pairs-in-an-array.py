from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        
        count = Counter(nums)
        res = 0
        
        if k == 0:
            for val in count:
                if count[val] > 1:
                    res += 1
        else:
            for val in count:
                if val + k in count:
                    res += 1
                    
        return res