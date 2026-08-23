"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None,
    bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)

        def build(r, c, size):
            first = grid[r][c]
            uniform = all(
                grid[r + i][c + j] == first
                for i in range(size)
                for j in range(size)
            )
            if uniform:
                return Node(val=bool(first), isLeaf=True)

            half = size // 2
            return Node(
                val=True,
                isLeaf=False,
                topLeft=build(r, c, half),
                topRight=build(r, c + half, half),
                bottomLeft=build(r + half, c, half),
                bottomRight=build(r + half, c + half, half),
            )

        return build(0, 0, n)