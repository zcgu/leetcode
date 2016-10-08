# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prehead = ListNode(0)
        prehead.next = head
        
        p = prehead
        
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                tmp = p.next.val
                while p.next and p.next.val == tmp:
                    p.next = p.next.next
            else:
                p = p.next
                
        return prehead.next