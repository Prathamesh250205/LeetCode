from collections import deque

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.dq = deque()
        self.capacity = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.dq.appendleft(value)
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.dq.append(value)
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.dq.popleft()
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.dq.pop()
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.dq[0]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.dq[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.dq) == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.dq) == self.capacity