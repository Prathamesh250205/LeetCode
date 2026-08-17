class Solution(object):
    def buildTree(self, inorder, postorder):
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            index = idx_map[val]
            
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root
            
        return helper(0, len(inorder) - 1)