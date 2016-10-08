class LinkList:
    def __init__(self, key):
        self.val = key
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # self.c = capacity
        # self.lst = []
        
        self.c = capacity
        self.table = {}
        self.head = LinkList(0)
        self.tail = LinkList(0)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def get(self, key):
        """
        :rtype: int
        """
        # for i, pair in enumerate(self.lst):
        #     if pair[0] == key:
        #         del self.lst[i]
        #         self.lst.append(pair)
        #         return pair[1]
        # return -1
        
        if key not in self.table:
            return -1
        
        value, node = self.table[key]
        
        node.prev.next, node.next.prev = node.next, node.prev
        self.tail.prev.next, self.tail.prev, node.prev, node.next = node, node, self.tail.prev, self.tail
        
        return value
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        # for i, pair in enumerate(self.lst):
        #     if pair[0] == key:
        #         del self.lst[i]
        #         pair[1] = value
        #         self.lst.append(pair)
        #         return 
        
        # if len(self.lst) == self.c:
        #     del self.lst[0]
                
        # self.lst.append([key, value])
        
        if self.get(key) != -1:
            self.table[key] = [value, self.table[key][1]]
            return
        
        if len(self.table) == self.c:
            node = self.head.next
            node.next.prev, self.head.next = self.head, node.next
            del self.table[node.val]
        
        node = LinkList(key)
        self.tail.prev.next, self.tail.prev, node.prev, node.next = node, node, self.tail.prev, self.tail
        self.table[key] = [value, node]
        
        
        
        