# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge(head)
    
    def merge(self, head):
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        h1 = self.merge(slow.next)
        slow.next = None
        h2 = self.merge(head)
        
        prehead = ListNode(0)
        tail = prehead
        while h1 or h2:
            if not h1:
                tail.next, tail, h2 = h2, h2, h2.next
            elif not h2:
                tail.next, tail, h1 = h1, h1, h1.next
            elif h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        return prehead.next        