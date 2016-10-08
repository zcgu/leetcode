# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
            
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        
        k = k % length
        
        p1 = p2 = head
        for _ in range(k):
            p2 = p2.next
            
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = head
        res = p1.next
        p1.next = None
        return res