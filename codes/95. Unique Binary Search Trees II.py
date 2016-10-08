# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        
        return self.helper(1, n)
        
    def helper(self, a, b):
        res = []
        
        if a > b:
            return [None]
        
        for val in range(a, b+1):
            for left in self.helper(a, val-1):
                for right in self.helper(val + 1, b):
                    node = TreeNode(val)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res