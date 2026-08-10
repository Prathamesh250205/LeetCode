from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        self.queue = deque()

        # BFS to find all nodes that aren't fully filled
        bfs_queue = deque([root])
        while bfs_queue:
            node = bfs_queue.popleft()
            if node.left:
                bfs_queue.append(node.left)
            if node.right:
                bfs_queue.append(node.right)
            if not node.left or not node.right:
                self.queue.append(node)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        new_node = TreeNode(v)
        parent = self.queue[0]

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.queue.popleft()  # parent is now full

        self.queue.append(new_node)
        return parent.val

    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()