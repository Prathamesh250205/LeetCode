# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        first_critical = -1
        prev_critical = -1
        min_dist = float('inf')

        prev = head
        curr = head.next if head else None
        idx = 1

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                if first_critical == -1:
                    first_critical = idx
                else:
                    min_dist = min(min_dist, idx - prev_critical)
                prev_critical = idx

            prev = curr
            curr = curr.next
            idx += 1

        if first_critical == -1 or prev_critical == first_critical:
            return [-1, -1]

        max_dist = prev_critical - first_critical
        return [min_dist, max_dist]