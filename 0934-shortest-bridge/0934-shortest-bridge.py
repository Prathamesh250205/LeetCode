class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def get_first_island():
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        return r, c
            return None


        start_r, start_c = get_first_island()
        stack = [(start_r, start_c)]
        grid[start_r][start_c] = 2
        island = [(start_r, start_c)]

        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    stack.append((nr, nc))
                    island.append((nr, nc))

 
        queue = island[:]
        steps = 0

        while queue:
            next_queue = []
            for r, c in queue:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            next_queue.append((nr, nc))
            queue = next_queue
            steps += 1

        return -1