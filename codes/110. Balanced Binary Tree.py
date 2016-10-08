# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.getH(root) != -1
    
    
    def getH(self, root):
        if not root:
            return 0
            
        h1 = self.getH(root.left)
        h2 = self.getH(root.right)
        
        if h1 == -1 or h2 == -1 or abs(h1 - h2) > 1:
            return -1
        
        return max(h1, h2) + 1