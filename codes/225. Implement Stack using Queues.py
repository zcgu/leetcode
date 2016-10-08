class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.list.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.list) == 0