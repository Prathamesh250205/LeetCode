class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parent = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        for x, y in stones:
            row = ('row', x)
            col = ('col', y)
            parent.setdefault(row, row)
            parent.setdefault(col, col)
            union(row, col)

        roots = {find(('row', x)) for x, y in stones}
        return len(stones) - len(roots)