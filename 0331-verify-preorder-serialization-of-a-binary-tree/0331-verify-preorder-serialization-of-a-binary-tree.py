class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        slots = 1  # available slots for the next node

        for node in nodes:
            if slots <= 0:
                return False
            if node == '#':
                slots -= 1
            else:
                slots -= 1
                slots += 2  # a non-null node opens 2 new slots

        return slots == 0