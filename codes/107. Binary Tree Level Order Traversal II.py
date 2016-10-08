# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        lst = [[root, 0]]
        i = 0
        while i < len(lst):
            node, lvl = lst[i]
            if node.left:
                lst.append([node.left, lvl+1])
            if node.right:
                lst.append([node.right, lvl+1])
            i += 1
        
        res = []
        tmp = []
        cur = 0
        for i in range(len(lst)):
            node, lvl = lst[i]
            if lvl == cur:
                tmp.append(node.val)
            else:
                res.append(tmp)
                tmp = [node.val]
                cur = lvl
        if tmp:
            res.append(tmp)
        res.reverse()
        return res
        