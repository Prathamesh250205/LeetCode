"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_vals = []
            next_queue = []
            for node in queue:
                level_vals.append(node.val)
                next_queue.extend(node.children)
            result.append(level_vals)
            queue = next_queue

        return result