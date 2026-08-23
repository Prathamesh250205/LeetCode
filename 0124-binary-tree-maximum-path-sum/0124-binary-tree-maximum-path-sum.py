# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.best = float('-inf')

        def gain(node):
            if not node:
                return 0
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)

            self.best = max(self.best, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        gain(root)
        return self.best