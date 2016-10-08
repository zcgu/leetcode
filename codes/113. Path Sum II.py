# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        
        self.helper(root, target, [])
        
        return self.res
    
    def helper(self, node, target, lst):
        if not node:
            return
        
        if not node.left and not node.right and sum(lst) + node.val == target:
            self.res.append(lst + [node.val])
            return
        
        self.helper(node.left, target, lst + [node.val])
        self.helper(node.right, target, lst + [node.val])
        
        