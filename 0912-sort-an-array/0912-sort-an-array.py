class Solution(object):
    def sortArray(self, nums):
        def merge_sort(arr, temp, left, right):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(arr, temp, left, mid)
            merge_sort(arr, temp, mid + 1, right)

            i, j, k = left, mid + 1, left
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            for idx in range(left, right + 1):
                arr[idx] = temp[idx]

        n = len(nums)
        temp = [0] * n
        merge_sort(nums, temp, 0, n - 1)
        return nums