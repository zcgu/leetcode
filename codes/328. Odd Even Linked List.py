# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        h1 = head
        h2 = head.next
        
        t1 = head
        t2 = head.next
        
        
        while t2 and t2.next:
            t2.next, t1.next, t1.next.next = t2.next.next, t2.next, h2
            t2 = t2.next
            t1 = t1.next
            
        return h1
        
        