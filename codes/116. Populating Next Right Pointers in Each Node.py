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
        head = root
        
        while head and head.left:
            nexthead = head.left
            
            while head:
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                    
                head = head.next
            
            head = nexthead
        
        
        
