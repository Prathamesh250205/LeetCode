class Solution(object):
    def countRatioSubarrays(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        n = len(nums)

        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + (b if v % 2 == 0 else -a)


        def merge_count(arr):
            n = len(arr)
            if n <= 1:
                return arr, 0
            mid = n // 2
            left, c1 = merge_count(arr[:mid])
            right, c2 = merge_count(arr[mid:])
            merged = []
            i = j = 0
            count = c1 + c2
            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    count += len(left) - i
                    merged.append(right[j])
                    j += 1
                else:
                    merged.append(left[i])
                    i += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, count

        return merge_count(prefix)[1]