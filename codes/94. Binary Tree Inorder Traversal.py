# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        que = [(root, False)]
        
        while que:
            node, visited = que.pop()
            
            if not node:
                continue
            elif not visited:
                que.append([node.right, False])
                que.append([node, True])
                que.append([node.left, False])
            else:
                res.append(node.val)
        return res