# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recur(root)
        return
    
    def recur(self, node):
        if not node:
            return None, None
            
        headl, taill = self.recur(node.left)
        headr, tailr = self.recur(node.right)
        
        if not headl and not headr:
            return node, node
        if not headl:
            node.left, node.right = None, headr
            return node, tailr
        if not headr:
            node.left, node.right = None, headl
            return node, taill
        else:
            node.left, node.right = None, headl
            taill.left, taill.right = None, headr
            return node, tailr