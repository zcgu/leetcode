# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(-2**31)
        
        cur = head
        
        while cur:
            # print cur.val
            p = h
            
            while p.next and p.next.val < cur.val:
                p = p.next
            
            p.next, cur.next, cur = cur, p.next, cur.next
        
        return h.next
            