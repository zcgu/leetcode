# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = 0
        self.inorder(root)
        return self.res
        
        
    def inorder(self, node):
        if not node: return
    
        self.inorder(node.left)
        
        if self.k == 0: return
    
        self.k -= 1
        
        if self.k == 0:
            self.res = node.val
            return
        
        self.inorder(node.right)
        
        
        
        
        
    #     return self.helper(root, k)[0]
        
    # def helper(self, node, k):
    #     if not node:
    #         return 0, False, 0
        
    #     val, found, num = self.helper(node.left, k)
        
    #     if found:
    #       return val, True, num
          
    #     if k - num == 1:
    #         return node.val, True, 0
        
    #     val2, found2, num2 = self.helper(node.right, k - num - 1)
        
    #     if found2:
    #         return val2, True, num2
        
    #     return 0, False, num + 1 + num2