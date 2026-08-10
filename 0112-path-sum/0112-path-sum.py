# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        remaining = targetSum - root.val

        if root.left is None and root.right is None:
            return remaining == 0

        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)