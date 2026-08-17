class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        curr = self.stack.pop()
        if curr.right:
            self._push_left(curr.right)
        return curr.val

    def hasNext(self):
        return len(self.stack) > 0