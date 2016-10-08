# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pre = root
        cur = None
        
        while pre and pre.left:
            cur = pre
            
            while cur:
                cur.left.next = cur.right
            
                if cur.next:
                    cur.right.next = cur.next.left
                    
                cur = cur.next
            
            pre = pre.left

        