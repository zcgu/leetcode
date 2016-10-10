# Given a non-negative number represented as a singly linked list of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Example:
# Input:
# 1->2->3

# Output:
# 1->2->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return ListNode(1)
        
        head2 = None
        while head:
            head.next, head, head2 = head2, head.next, head
        
        carry = 1
        p = head2
        while carry == 1:
            p.val += 1
            carry = p.val / 10
            p.val %= 10
            
            if p.next:
                p = p.next
            else:
                break
        
        if carry == 1:
            p.next = ListNode(1)
        
        while head2:
            head2.next, head2, head = head, head2.next, head2
        
        return head
        
        
        
        
