# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        lst = [[root, 1]]
        
        i = 0
        while i < len(lst):
            node, lvl = lst[i]
            
            if node.left:
                lst.append([node.left, lvl+1])
            if node.right:
                lst.append([node.right, lvl+1])
            
            i += 1
        
        lvl = 1
        tmp = []
        res = []
        while lst:
            if lst[0][1] == lvl:
                tmp.append(lst[0][0].val)
                del lst[0]
            else:
                res.append(tmp)
                tmp = []
                lvl += 1
        if tmp:
            res.append(tmp)
        
        return res