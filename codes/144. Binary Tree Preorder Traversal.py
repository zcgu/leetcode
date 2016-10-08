# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        lst = [root]
        res = []
        
        while lst:
            node = lst.pop()
            if node:
                res.append(node.val)
                lst.append(node.right)
                lst.append(node.left)
            
        return res