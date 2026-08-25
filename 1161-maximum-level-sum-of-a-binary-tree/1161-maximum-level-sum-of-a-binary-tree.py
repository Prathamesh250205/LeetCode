# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        best_level = 1
        best_sum = float('-inf')
        level = 1
        queue = [root]

        while queue:
            level_sum = sum(node.val for node in queue)
            if level_sum > best_sum:
                best_sum = level_sum
                best_level = level

            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            level += 1

        return best_level