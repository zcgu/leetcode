# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.cur = None
        self.res = True
        
        self.recur(root)
        
        return self.res
        
    def recur(self, node):
        if not node:
            return
        
        self.recur(node.left)
        
        if node.val <= self.cur:
            self.res = False
            return
        self.cur = node.val
        
        self.recur(node.right)