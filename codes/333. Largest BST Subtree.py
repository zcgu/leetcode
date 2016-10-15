# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

# Note:
# A subtree must include all of its descendants.
# Here's an example:
#     10
#     / \
#    5  15
#   / \   \ 
#  1   8   7
# The Largest BST Subtree in this case is the highlighted one. 
# The return value is the subtree's size, which is 3.
# Hint:

# You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.postorder(root)
        return self.res

    def postorder(self, root):
        if not root: return None, None, True, 0

        min1, max1, isbst1, size1 = self.postorder(root.left)
        min2, max2, isbst2, size2 = self.postorder(root.right)

        if min1 is None and min2 is None:
            self.res = max(self.res, 1)
            return root.val, root.val, True, 1
        elif min2 is None:
            if root.val > max1 and isbst1:
                self.res = max(self.res, size1 + 1)
                return min1, root.val, True, size1 + 1
            else:
                return 0, 0, False, 0
        elif min1 is None:
            if root.val < min2 and isbst2:
                self.res = max(self.res, size2 + 1)
                return root.val, max2, True, size2 + 1
            else:
                return 0, 0, False, 0
        else:
            if isbst1 and isbst2 and root.val > max1 and root.val < min2:
                self.res = max(self.res, size1 + size2 + 1)
                return min1, max2, True, size1 + size2 + 1
            else:
                return 0, 0, False, 0

