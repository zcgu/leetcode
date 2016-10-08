# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        que = [(root, 1)]
        i = 0
        while i < len(que):
            node, lvl = que[i]
            if node.left:
                que.append([node.left, lvl+1])
            if node.right:
                que.append([node.right, lvl+1])
            i += 1
        
        res = [[que[0][0].val]]
        for i in range(1, len(que)):
            if que[i][1] == que[i-1][1]:
                res[-1].append(que[i][0].val)
            else:
                res.append([que[i][0].val])
        
        for i in range(1, len(res), 2):
            res[i].reverse()
        
        return res
        
        