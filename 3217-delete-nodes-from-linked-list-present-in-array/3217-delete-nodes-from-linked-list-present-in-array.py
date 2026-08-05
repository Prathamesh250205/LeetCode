# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        to_remove = set(nums)
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val in to_remove:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next