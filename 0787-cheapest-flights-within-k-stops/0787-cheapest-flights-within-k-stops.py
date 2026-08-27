class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_dist = dist[:]
            for u, v, w in flights:
                if dist[u] != float('inf') and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist

        return dist[dst] if dist[dst] != float('inf') else -1