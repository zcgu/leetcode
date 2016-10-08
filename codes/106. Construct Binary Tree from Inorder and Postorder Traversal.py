# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        return self.helper(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
        
    def helper(self, inorder, postorder, lin, rin, lpost, rpost):
        if not inorder or lin > rin:
            return None
        
        root = TreeNode(postorder[rpost])
        
        index1 = inorder.index(root.val)
        index2 = lpost + index1 - lin
        
        root.left = self.helper(inorder, postorder, lin, index1-1, lpost, index2-1)
        root.right = self.helper(inorder, postorder, index1+1, rin, index2, rpost-1)
        
        return root