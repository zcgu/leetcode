# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
        
    def helper(self, root):
        if not root:
            return [-2**31, - 2**31]
        if not root.left and not root.right:
            return [root.val, -2**31]

        l = self.helper(root.left)
        r = self.helper(root.right)
        
        return [max(root.val, root.val + l[0], root.val + r[0]), max(max(l), max(r), root.val + max(l[0],0) + max(r[0],0))]
        