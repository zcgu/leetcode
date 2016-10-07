# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = self.depth(root, True)
        right = self.depth(root, False)
        
        if left == right:
            return 2 ** left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        

    def depth(self, node, isleft):
        res = 0
        
        while node:
            res += 1
            node = node.left if isleft else node.right
        
        return res
        
        