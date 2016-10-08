class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # [[x, curMin]]
        self.lst = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.lst:
            self.lst.append([x, x])
        else:
            if x < self.lst[-1][1]:
                self.lst.append([x, x])
            else:
                self.lst.append([x, self.lst[-1][1]])

    def pop(self):
        """
        :rtype: void
        """
        return self.lst.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.lst[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()