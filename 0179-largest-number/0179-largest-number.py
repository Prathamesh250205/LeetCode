from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        strs = [str(n) for n in nums]
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0
        
        strs.sort(key=cmp_to_key(compare))
        result = ''.join(strs)
        return '0' if result[0] == '0' else result