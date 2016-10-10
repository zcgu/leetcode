# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

# For example:
# Given a binary tree {1,2,3,4,5},
#     1
#    / \
#   2   3
#  / \
# 4   5
# return the root of the binary tree [4,5,2,#,#,3,1].
#    4
#   / \
#  5   2
#     / \
#    3   1  
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 这个题就是把left recursive一下，rightrecursive一下，然后和root三个人调换位置。
        head, tail = self.dfs(root)
        return head
        
    def dfs(self, root):
        if not root: return None, None
        if not root.left: return root, root
        
        head1, tail1 = self.dfs(root.left)
        head2, tail2 = self.dfs(root.right)
        
        tail1.right = root
        tail1.left = head2
        
        root.left = None    # 这个是挺容易忘。
        root.right = None
        
        return head1, root
        
