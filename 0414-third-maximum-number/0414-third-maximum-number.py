class Solution(object):
    def thirdMax(self, nums):
        distinct = list(set(nums))
        if len(distinct) < 3:
            return max(distinct)
        distinct.sort(reverse=True)
        return distinct[2]