class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        
        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'
            
            found = (backtrack(row + 1, col, index + 1) or
                     backtrack(row - 1, col, index + 1) or
                     backtrack(row, col + 1, index + 1) or
                     backtrack(row, col - 1, index + 1))
            
            board[row][col] = temp
            
            return found
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False