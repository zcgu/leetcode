# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        res = 1
        if root.left:
            res = max(res, 1 + self.maxDepth(root.left))
        
        if root.right:
            res = max(res, 1 + self.maxDepth(root.right))
        return res