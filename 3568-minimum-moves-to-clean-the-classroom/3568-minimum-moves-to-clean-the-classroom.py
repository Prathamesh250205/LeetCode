from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m, n = len(classroom), len(classroom[0])
        litter_index = {}
        start = None

        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    litter_index[(i, j)] = len(litter_index)

        total_litter = len(litter_index)
        if total_litter == 0:
            return 0

        full_mask = (1 << total_litter) - 1
        start_mask = full_mask
        if start in litter_index:
            start_mask &= ~(1 << litter_index[start])

        num_masks = 1 << total_litter
        # best_energy[x][y][mask] = highest energy ever achieved at that
        # (position, remaining-litter) state -- since more energy is never
        # worse, a state reached with <= energy than one already seen is
        # always dominated and can be skipped entirely.
        best_energy = [[[-1] * num_masks for _ in range(n)] for _ in range(m)]
        sx, sy = start
        best_energy[sx][sy][start_mask] = energy

        queue = deque([(sx, sy, energy, start_mask)])
        moves = 0

        while queue:
            for _ in range(len(queue)):
                x, y, cur_energy, mask = queue.popleft()

                if mask == 0:
                    return moves

                if cur_energy == 0:
                    continue

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                        cell = classroom[nx][ny]
                        next_energy = energy if cell == 'R' else cur_energy - 1
                        next_mask = mask
                        if (nx, ny) in litter_index:
                            next_mask &= ~(1 << litter_index[(nx, ny)])

                        if next_energy > best_energy[nx][ny][next_mask]:
                            best_energy[nx][ny][next_mask] = next_energy
                            queue.append((nx, ny, next_energy, next_mask))

            moves += 1

        return -1