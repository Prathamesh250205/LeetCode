# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self._check(root, root.val)

    def _check(self, node, value):
        if node is None:
            return True
        if node.val != value:
            return False
        return self._check(node.left, value) and self._check(node.right, value)