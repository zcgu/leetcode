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

        l = self.helper(root.left)
        r = self.helper(root.right)
        
        a = max(root.val, left[0] + root.val, right[0] + root.val)
        return [a, max(a, max(left), max(right), left[0] + root.val + right[0])]
