# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        h = ListNode(0)
        h.next = head
        
        fast = h
        slow = h
        
        for i in range(n):
            fast = fast.next
            if not fast:
                return h.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return h.next