# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = t1 = ListNode(0)
        h2 = t2 = ListNode(0)
        
        p = head
        while p:
            if p.val < x:
                t1.next = p
                t1 = t1.next
                p = p.next
                t1.next = None
            else:
                t2.next = p
                t2 = t2.next
                p = p.next
                t2.next = None
        
        if h1.next:
            t1.next = h2.next
            return h1.next
        else:
            return h2.next
            