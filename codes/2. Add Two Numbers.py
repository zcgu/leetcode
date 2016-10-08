# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead = ListNode(0)
        tail = prehead
        
        a = 0
        
        p1 = l1
        p2 = l2
        
        while p1 or p2:
            number = a
            if p1:
                number += p1.val
                p1 = p1.next
            if p2:
                number += p2.val
                p2 = p2.next
            node = ListNode(number % 10)
            a = number / 10
            tail.next = node
            tail = node
        
        
        if a != 0:
            node = ListNode(1)
            tail.next = node
        
        return prehead.next
            