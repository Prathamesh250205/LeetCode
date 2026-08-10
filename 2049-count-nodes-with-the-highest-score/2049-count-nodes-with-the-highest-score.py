class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        subtree_size = [1] * n

        
        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            for child in children[node]:
                stack.append(child)

        for node in reversed(order):
            for child in children[node]:
                subtree_size[node] += subtree_size[child]

        max_score = 0
        count = 0

        for node in range(n):
            score = 1
            remaining = n - subtree_size[node]
            if remaining > 0:
                score *= remaining
            for child in children[node]:
                score *= subtree_size[child]

            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1

        return count