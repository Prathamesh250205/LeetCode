class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        def get_coords(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            actual_row = n - 1 - row
            return actual_row, col

        visited = [False] * (n * n + 1)
        visited[1] = True
        queue = [(1, 0)]  # (square, moves)

        while queue:
            next_queue = []
            for square, moves in queue:
                if square == n * n:
                    return moves
                for die in range(1, 7):
                    nxt = square + die
                    if nxt > n * n:
                        break
                    r, c = get_coords(nxt)
                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if not visited[nxt]:
                        visited[nxt] = True
                        next_queue.append((nxt, moves + 1))
            queue = next_queue

        return -1