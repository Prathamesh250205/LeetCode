"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        mapping = {}

        node = head
        while node:
            mapping[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            mapping[node].next = mapping.get(node.next)
            mapping[node].random = mapping.get(node.random)
            node = node.next

        return mapping[head]