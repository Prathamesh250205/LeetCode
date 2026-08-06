class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        self.curr = head

        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2

            left_child = build(left, mid - 1)

            root = TreeNode(self.curr.val)
            root.left = left_child
            self.curr = self.curr.next

            root.right = build(mid + 1, right)

            return root

        return build(0, size - 1)