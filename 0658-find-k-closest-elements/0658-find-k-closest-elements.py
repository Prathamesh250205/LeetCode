import bisect

class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1

        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]