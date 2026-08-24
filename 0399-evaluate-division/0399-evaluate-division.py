class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for (a, b), v in zip(equations, values):
            graph.setdefault(a, {})[b] = v
            graph.setdefault(b, {})[a] = 1.0 / v

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0

            visited = {src}
            queue = [(src, 1.0)]

            while queue:
                node, acc = queue.pop(0)
                for neighbor, weight in graph[node].items():
                    if neighbor == dst:
                        return acc * weight
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, acc * weight))

            return -1.0

        return [bfs(c, d) for c, d in queries]