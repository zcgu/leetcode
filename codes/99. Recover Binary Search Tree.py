# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        
        # 这个pre精髓
        self.pre = None
        
        self.inorder(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val
    
        
    def inorder(self, root):
        if not root: return
        
        self.inorder(root.left)
    
        if not self.first and self.pre and self.pre.val > root.val:
            self.first = self.pre
        
        # 这个不是elif是if，因为可能是两个连一起换的。
        # 先把第二个设置了，如果后面再有再换成新的第二个
        if self.first and self.pre and self.pre.val > root.val:
            self.second = root
            
        self.pre = root
        
        self.inorder(root.right)
        
        
        
