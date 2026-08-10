from collections import deque

class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        n = len(parent)
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)

        self.locked_by = [-1] * n
        self.locked_descendant_count = [0] * n

    def _update_ancestors(self, num, delta):
        node = self.parent[num]
        while node != -1:
            self.locked_descendant_count[node] += delta
            node = self.parent[node]

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked_by[num] != -1:
            return False
        self.locked_by[num] = user
        self._update_ancestors(num, 1)
        return True

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked_by[num] != user:
            return False
        self.locked_by[num] = -1
        self._update_ancestors(num, -1)
        return True

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked_by[num] != -1:
            return False
        if self.locked_descendant_count[num] == 0:
            return False

        node = self.parent[num]
        while node != -1:
            if self.locked_by[node] != -1:
                return False
            node = self.parent[node]

        queue = deque([num])
        while queue:
            curr = queue.popleft()
            for child in self.children[curr]:
                if self.locked_by[child] != -1:
                    self.locked_by[child] = -1
                    self._update_ancestors(child, -1)
                queue.append(child)

        self.locked_by[num] = user
        self._update_ancestors(num, 1)
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)