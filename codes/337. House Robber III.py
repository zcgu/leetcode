# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.value(root))
        
    def value(self, node):
        if not node:
            return [0, 0]
        
        v1 = self.value(node.left)
        v2 = self.value(node.right)
        
        return [node.val + v1[1] + v2[1], max(v1) + max(v2)]