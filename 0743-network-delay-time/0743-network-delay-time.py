import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                nd = d + weight
                if nd < dist[neighbor]:
                    dist[neighbor] = nd
                    heapq.heappush(heap, (nd, neighbor))

        max_dist = max(dist[1:])
        return max_dist if max_dist != float('inf') else -1