class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: Optional[ListNode]
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False

        if self.matchPath(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def matchPath(self, head, node):
        if not head:
            return True
        if not node or node.val != head.val:
            return False
        return self.matchPath(head.next, node.left) or self.matchPath(head.next, node.right)