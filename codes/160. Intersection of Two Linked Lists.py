# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        lenA = 0
        p1 = headA
        while p1:
            lenA += 1
            p1 = p1.next
            
        lenB = 0
        p2 = headB
        while p2:
            lenB += 1
            p2 = p2.next
        
        p1 = headA
        p2 = headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                p1 = p1.next
        elif lenA < lenB:
            for _ in range(lenB - lenA):
                p2 = p2.next
        
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        
        return None
            