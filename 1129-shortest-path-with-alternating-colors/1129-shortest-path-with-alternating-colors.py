class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        RED, BLUE = 0, 1
        graph = [[[] for _ in range(2)] for _ in range(n)]

        for a, b in redEdges:
            graph[a][RED].append(b)
        for a, b in blueEdges:
            graph[a][BLUE].append(b)

        # state = (node, color of edge used to arrive)
        visited = [[False] * 2 for _ in range(n)]
        dist = [-1] * n
        dist[0] = 0
        visited[0][RED] = True
        visited[0][BLUE] = True

        queue = [(0, RED), (0, BLUE)]
        steps = 0

        while queue:
            next_queue = []
            steps += 1
            for node, last_color in queue:
                next_color = 1 - last_color
                for neighbor in graph[node][next_color]:
                    if not visited[neighbor][next_color]:
                        visited[neighbor][next_color] = True
                        if dist[neighbor] == -1:
                            dist[neighbor] = steps
                        next_queue.append((neighbor, next_color))
            queue = next_queue

        return dist