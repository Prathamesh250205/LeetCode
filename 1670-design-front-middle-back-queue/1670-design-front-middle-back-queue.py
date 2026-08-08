from collections import deque

class FrontMiddleBackQueue(object):

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _balance(self):
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left):
            self.left.append(self.right.popleft())

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        self._balance()

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.right.append(val)
        self._balance()

    def popFront(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self._balance()
        return val

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if len(self.left) >= len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self._balance()
        return val

    def popBack(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._balance()
        return val