# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        if not head:
            return None
            
        prehead = ListNode(0)
        prehead.next = head
        
        p = prehead
        
        while True:
            tmp = p
            for _ in range(k):
                tmp = tmp.next
                if not tmp:
                    return prehead.next
            
            tail = p.next
            head2 = p.next.next
            tail.next = None
            
            for _ in range(k-1):
                p.next, head2.next, head2 = head2, p.next, head2.next
            
            tail.next = head2
            p = tail