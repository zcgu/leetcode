# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        prehead = ListNode(0)
        prehead.next = head
        
        count = 1
        tail1 = prehead
        while count < m:
            tail1 = tail1.next
            count += 1
        
        if not tail1 or not tail1.next:
            return head
        
        tail2 = tail1.next
        head2 = tail1.next.next
        
        for _ in range(n-m):
            tail1.next, head2.next, head2 = head2, tail1.next, head2.next
        
        tail2.next = head2
        
        return prehead.next