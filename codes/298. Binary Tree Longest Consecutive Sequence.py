# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.postorder(root)
        return self.res

    def postorder(self, node):
        if not node: return 0
        
        num1 = self.postorder(node.left)
        num2 = self.postorder(node.right)
    
        res = 1
        if num1 > 0 and node.val == node.left.val - 1:
            res = max(res, 1 + num1)
        if num2 > 0 and node.val == node.right.val - 1:
            res = max(res, 1 + num2)
        self.res = max(self.res, res)
        return res


