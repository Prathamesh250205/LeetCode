import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(min(n, k))]
        heapq.heapify(heap)
        
        result = None
        for _ in range(k):
            result, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        
        return result