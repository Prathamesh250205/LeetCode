"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def traverse(node):
            if node is None:
                return
            for child in node.children:
                traverse(child)
            result.append(node.val)

        traverse(root)
        return result