class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0] * n  # 0 = uncolored, 1/-1 = the two sides

        for start in range(n):
            if color[start] != 0:
                continue
            color[start] = 1
            queue = [start]
            while queue:
                node = queue.pop()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False

        return True