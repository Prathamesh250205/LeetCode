import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        heap = [(arr[i] / float(arr[n - 1]), i, n - 1) for i in range(n - 1)]
        heapq.heapify(heap)

        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / float(arr[j - 1]), i, j - 1))

        _, i, j = heap[0]
        return [arr[i], arr[j]]