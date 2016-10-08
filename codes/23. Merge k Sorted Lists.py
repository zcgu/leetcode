# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import *
        hp = []
        
        for node in lists:
            if node:
                heappush(hp, (node.val, node))
        
        h = ListNode(0)
        p = h
        while hp:
            p.next = heappop(hp)[1]
            p = p.next
            if p.next:
                heappush(hp, (p.next.val, p.next))
        return h.next