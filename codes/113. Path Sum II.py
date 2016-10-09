# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return self.dfs(root, sum)
        
    def dfs(self, root, sums):
        if not root: return []
        
        if not root.left and not root.right:
            if root.val == sums:
                return [[root.val]]
            else:
                return []
        
        res = []
        
        for lst in self.dfs(root.left, sums - root.val):
            res.append([root.val] + lst)
        for lst in self.dfs(root.right, sums - root.val):
            res.append([root.val] + lst)
        
        return res
        
        
        
