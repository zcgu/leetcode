# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # divide
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        h1 = head
        h2 = slow.next
        slow.next = None
        
        # reverse
        tail = None
        while h2:
            h2.next, h2, tail = tail, h2.next, h2
        h2 = tail
        
        # insert
        while h1 and h2:
            h1.next, h1, h2.next, h2 = h2, h1.next, h1.next, h2.next
        return