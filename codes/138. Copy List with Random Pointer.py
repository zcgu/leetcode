# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
         
        p = head
        while p:
            node = RandomListNode(p.label)
            node.random = p.random
            p.next, p, node.next = node, p.next, p.next
        
        p = head.next
        while p:
            if p.random:
                p.random = p.random.next
            if not p.next or not p.next.next:
                break
            p = p.next.next
            
        prehead = RandomListNode(0)
        tail = prehead
        p = head
        while p and p.next:
            p.next, p, tail.next, tail = p.next.next, p.next.next, p.next, p.next
        
        tail.next = None
        
        return prehead.next
        
        