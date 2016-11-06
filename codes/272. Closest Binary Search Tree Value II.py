# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# Hint:

# Consider implement these two helper functions:
# getPredecessor(N), which returns the next smaller node to N.
# getSuccessor(N), which returns the next larger node to N.
# Try to assume that each node has a parent pointer, it makes the problem much easier.
# Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
# You would need two stacks to track the path in finding predecessor and successor node separately.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def closestKValues(self, root, target, k):
#         """
#         :type root: TreeNode
#         :type target: float
#         :type k: int
#         :rtype: List[int]
#         """
#         if not root: return []
#         self.lst = []
    
#         self.dfs(root, target, k)

#         return [pair[1] for pair in self.lst]


    
#     def dfs(self, root, target, k):
#         if not root: return
        
#         from bisect import bisect_left
#         index = bisect_left(self.lst, (abs(root.val - target), root.val))
#         self.lst.insert(index, (abs(root.val - target), root.val))

#         if len(self.lst) > k:
#           self.lst.pop()
        
#         self.dfs(root.left, target, k)
#         self.dfs(root.right, target, k)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack1 = []
        stack2 = []
        
        cur = root
        while cur:
            if cur.val <= target:
                stack1.append(cur)
                cur = cur.right
            else:
                stack2.append(cur)
                cur = cur.left
        
        res = []
        for _ in range(k):
            if not stack1 and not stack2:
                return res
            elif not stack2:
                node = self.nextSmaller(stack1)
                res.append(node.val)
            elif not stack1:
                node = self.nextLarger(stack2)
                res.append(node.val)
            elif abs(stack1[-1].val - target) < abs(stack2[-1].val - target):
                node = self.nextSmaller(stack1)
                res.append(node.val)
            else:
                node = self.nextLarger(stack2)
                res.append(node.val)
        return res
    
    
    
    
    def nextLarger(self, stack):
        node = stack.pop()
        
        p = node.right
        while p:
            stack.append(p)
            p = p.left
        
        return node
    
    def nextSmaller(self, stack):
        node = stack.pop()
        
        p = node.left
        while p:
            stack.append(p)
            p = p.right
        
        return node
    
    
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def closestKValues(self, root, target, k):
#         """
#         :type root: TreeNode
#         :type target: float
#         :type k: int
#         :rtype: List[int]
#         """
#         if not root: return []
#         self.lst = []
    
#         self.dfs(root, target, k)

#         return [pair[1] for pair in self.lst]


    
#     def dfs(self, root, target, k):
#         if not root: return
        
#         from bisect import bisect_left
#         index = bisect_left(self.lst, (abs(root.val - target), root.val))
#         self.lst.insert(index, (abs(root.val - target), root.val))

#         if len(self.lst) > k:
#           self.lst.pop()
        
#         self.dfs(root.left, target, k)
#         self.dfs(root.right, target, k)


        
        
        
        
