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
        return self.build(head)
            
    def build(self, head):
        if not head: return None
        
        if not head.next: return TreeNode(head.val)     # 这个是因为要fast=head.next.next
        
        slow = head
        fast = head.next.next           # 这里不容易写对
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        root = TreeNode(slow.next.val)
        
        slow.next, slow = None, slow.next.next
        
        root.left = self.build(head)
        root.right = self.build(slow)
        
        return root
        
        
        
        
        
        
#         2. 感觉不是正着啊
#         if not head:
#             return None
            
#         self.node = head
        
#         p = head
#         size = 0
#         while p:
#             p = p.next
#             size += 1
        
#         return self.treeHelper(1, size)
        
        
        
#     def treeHelper(self, a, b):
        
#         if a > b:
#             return None
            
#         mid = (a + b) / 2
#         left = self.treeHelper(a, mid-1)
        
#         tree = TreeNode(self.node.val)
        
#         self.node = self.node.next
#         tree.left = left
        
#         tree.right = self.treeHelper(mid+1, b)
        
#         return tree
        
        
