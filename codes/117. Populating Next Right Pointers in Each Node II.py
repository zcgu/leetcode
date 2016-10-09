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
    
    # 这两个题，只需要一个head和nexthead，链接head的下一个lvl。
    
    def connect(self, root):
        head = root
        
        while head:
            nexthead = None
            needNext = None
            
            while head:
                if head.left:
                    if not nexthead: nexthead = head.left
                    
                    if needNext:
                        needNext.next = head.left
                    
                    if head.right:
                        head.left.next = head.right
                        needNext = head.right
                    else:
                        needNext = head.left
                    
                elif head.right:
                    if not nexthead: nexthead = head.right
                    
                    if needNext:
                        needNext.next = head.right
                    
                    needNext = head.right
                
                head = head.next
            
            head = nexthead
            
