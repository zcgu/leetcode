# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.recur(root, 1)
        return self.res
        
    def recur(self, node, lvl):
        if not node:
            return
        if len(self.res) < lvl:
            self.res.append(node.val)
        self.recur(node.right, lvl + 1)
        self.recur(node.left, lvl + 1)