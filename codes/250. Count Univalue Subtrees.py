# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# For example:
# Given binary tree,
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# return 4.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root: return 0
        self.postorder(root)
        
        return self.res
        
    def postorder(self, root):
        if root.left:
            num1 = self.postorder(root.left)
        if root.right:
            num2 = self.postorder(root.right)
        
        if not root.left and not root.right:
            self.res += 1
            return root.val
        elif not root.left:
            if num2 is not None and num2 == root.val:
                self.res += 1
                return num2
            else:
                return None
        elif not root.right:
            if num1 is not None and num1 == root.val:
                self.res += 1
                return num1
            else:
                return None
        else:
            if num1 is not None and num2 is not None and num1 == num2 == root.val:
                self.res += 1
                return num1
            else:
                return None
            
            
