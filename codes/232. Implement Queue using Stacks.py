class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.lst.insert(0, x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        return self.lst.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.lst[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.lst) == 0