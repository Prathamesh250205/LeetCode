class Solution(object):
    def removeNodes(self, head):
        if head is None:
            return None

        head.next = self.removeNodes(head.next)

        if head.next is not None and head.next.val > head.val:
            return head.next

        return head