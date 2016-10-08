# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.res = []
        
        if not root:
            return []
            
        self.recur(root, "")
        return self.res
        
    def recur(self, root, s):
        if len(s) == 0:
            s += str(root.val)
        else:
            s += "->" + str(root.val)
            
        if not root.left and not root.right:
            self.res.append(s)
        elif root.left and root.right:
            self.recur(root.left, s)
            self.recur(root.right, s)
        elif root.left:
            self.recur(root.left, s)
        else:
            self.recur(root.right, s)
            