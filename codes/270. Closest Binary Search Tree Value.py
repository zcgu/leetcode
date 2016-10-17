# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root: return 0

        self.res = root.val
        
        self.dfs = self.dfs(root, target)

        return self.res

    def dfs(self, root, target):
        if not root: return

        if abs(root.val - target) < abs(self.res - target):
            self.res = root.val

        if root.val < target:
            self.dfs(root.right, target)
        elif root.val > target:
            self.dfs(root.left, target)
        else:
            return

