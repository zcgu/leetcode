# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples:

# Given binary tree [3,9,20,null,null,15,7],
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
# return its vertical order traversal as:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7],
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
# return its vertical order traversal as:
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# return its vertical order traversal as:
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        table = {}
        que = [(root, 0)]
        
        while que:
            node, lvl = que.pop(0)
            
            if not node: continue
        
            if lvl in table:
                table[lvl].append(node.val)
            else:
                table[lvl] = [node.val]
            
            que.append((node.left, lvl - 1))
            que.append((node.right, lvl + 1))
        
        lst = [item for item in table.items()]
        lst.sort()
        return [pair[1] for pair in lst]
        
        
