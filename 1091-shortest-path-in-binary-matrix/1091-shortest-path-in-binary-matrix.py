class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        if n == 1:
            return 1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        grid[0][0] = 1 
        queue = [(0, 0)]
        length = 1

        while queue:
            next_queue = []
            for r, c in queue:
                if r == n - 1 and c == n - 1:
                    return length
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        next_queue.append((nr, nc))
            queue = next_queue
            length += 1

        return -1