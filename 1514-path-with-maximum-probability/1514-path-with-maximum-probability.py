import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        prob = [0.0] * n
        prob[start_node] = 1.0
        # max-heap via negated probabilities
        heap = [(-1.0, start_node)]

        while heap:
            neg_p, node = heapq.heappop(heap)
            p = -neg_p
            if node == end_node:
                return p
            if p < prob[node]:
                continue
            for neighbor, edge_p in graph[node]:
                new_p = p * edge_p
                if new_p > prob[neighbor]:
                    prob[neighbor] = new_p
                    heapq.heappush(heap, (-new_p, neighbor))

        return 0.0