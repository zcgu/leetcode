# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if not fast or not fast.next:
                return None
            
            if fast == slow:
                break
        
        p = head
        while p != fast:
            p = p.next
            fast = fast.next
        return p
            