# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        rev = None
        
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, rev = rev, slow.next, slow
        
        if fast:
            slow = slow.next
        
        while rev:
            if rev.val != slow.val:
                return False
            rev, slow = rev.next, slow.next
            
        return True
        