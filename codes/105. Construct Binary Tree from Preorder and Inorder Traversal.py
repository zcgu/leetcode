# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
            
        return self.buildRecur(preorder, inorder, 0, len(preorder)- 1, 0, len(inorder) - 1)
    
    def buildRecur(self, preorder, inorder, p1, p2, i1, i2):
        
        if p1 > p2 or i1 > i2:
            return None
            
        val = preorder[p1]
        index = inorder.index(val)
        
        # i1 = inorder[:index]
        # i2 = inorder[index+1:]
        
        # p1 = preorder[1:1+len(i1)]
        # p2 = preorder[1+len(i1):]
        
        node = TreeNode(val)
        node.left = self.buildRecur(preorder, inorder, p1 + 1, p1 + 1 + index - 1 - i1, i1, index-1)
        node.right = self.buildRecur(preorder, inorder, p1 + 1 + index - i1, p2, index +1, i2)
        
        return node
        
        