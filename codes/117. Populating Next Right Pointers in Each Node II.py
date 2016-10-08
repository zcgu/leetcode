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
        
        nexthead = root
        
        while nexthead:
            cur = nexthead
            
            nexthead = None
            
            needlink = None
            
            while cur:
                if cur.left:
                    if needlink:
                        needlink.next = cur.left
                        
                    if cur.right:
                        cur.left.next = cur.right
                        needlink = cur.right
                    else:
                        needlink = cur.left
                        
                    if not nexthead:
                        nexthead = cur.left
                elif cur.right:
                    if needlink:
                        needlink.next = cur.right
                        
                    needlink = cur.right
                    
                    if not nexthead:
                        nexthead = cur.right
                
                cur = cur.next

                
                
            