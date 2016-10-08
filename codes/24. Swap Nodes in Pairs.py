# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        h = ListNode(0)
        h.next = head
        
        p = h
        while p and p.next and p.next.next:
            p1 = p.next
            p2 = p1.next
            p3 = p2.next
            
            p.next = p2
            p2.next = p1
            p1.next = p3
            
            p = p.next.next
        
        return h.next