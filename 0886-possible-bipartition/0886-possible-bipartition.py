class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (n + 1)  # 0 = uncolored, 1/-1 = the two groups

        def bfs(start):
            color[start] = 1
            queue = [start]
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            return True

        for person in range(1, n + 1):
            if color[person] == 0:
                if not bfs(person):
                    return False

        return True