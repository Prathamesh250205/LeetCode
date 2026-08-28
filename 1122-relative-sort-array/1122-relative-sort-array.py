class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        max_val = max(arr1)
        count = [0] * (max_val + 1)
        for x in arr1:
            count[x] += 1

        result = []

        for x in arr2:
            result.extend([x] * count[x])
            count[x] = 0

        for x in range(max_val + 1):
            if count[x] > 0:
                result.extend([x] * count[x])

        return result