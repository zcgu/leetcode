# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        self.lst = []
        self.recur(root, 0)
        return sum(self.lst)
        
    def recur(self, node, num):
        num = num * 10 + node.val
        
        if not node.left and not node.right:
            self.lst.append(num)
        
        if node.left:
            self.recur(node.left, num)
        
        if node.right:
            self.recur(node.right, num)