class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        indegree = [0] * n

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    indegree[child] += 1
                    if indegree[child] > 1:
                        return False  # a node has more than one parent

        # exactly one root: a node with no parent
        roots = [i for i in range(n) if indegree[i] == 0]
        if len(roots) != 1:
            return False

        # BFS/DFS from the root; must reach every node exactly once (no cycles)
        visited = set()
        stack = [roots[0]]
        while stack:
            node = stack.pop()
            if node in visited:
                return False  # cycle
            visited.add(node)
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    stack.append(child)

        return len(visited) == n