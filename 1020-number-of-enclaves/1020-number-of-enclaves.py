class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(sr, sc):
            grid[sr][sc] = 0
            queue = [(sr, sc)]
            while queue:
                r, c = queue.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

    
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and grid[r][c] == 1:
                    bfs(r, c)

        return sum(row.count(1) for row in grid)