# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        h = ListNode(0)
        tail = h
        
        while l1 or l2:
            if not l1:
                tail.next = l2
                return h.next
            
            if not l2:
                tail.next = l1
                return h.next
            
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
                tail.next = None
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
                tail.next = None
        
        return h.next