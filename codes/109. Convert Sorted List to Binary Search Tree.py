# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
            
        self.node = head
        
        p = head
        size = 0
        while p:
            p = p.next
            size += 1
        
        return self.treeHelper(1, size)
        
        
        
    def treeHelper(self, a, b):
        
        if a > b:
            return None
            
        mid = (a + b) / 2
        left = self.treeHelper(a, mid-1)
        
        tree = TreeNode(self.node.val)
        
        self.node = self.node.next
        tree.left = left
        
        tree.right = self.treeHelper(mid+1, b)
        
        return tree
        
        