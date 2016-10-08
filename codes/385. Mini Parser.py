# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # 1. 用stack
        
        if not s:
            return None
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        p = 0
        stack = []
        
        while p < len(s):
            if s[p] == '[':
                stack.append(s[p])
                p += 1
            elif s[p].isdigit() or s[p] == '-':             # '-' don't forget
                p2 = p + 1
                while p2 < len(s) and s[p2].isdigit():
                    p2 += 1
                stack.append(s[p:p2])
                p = p2
            elif s[p] == ',':
                p += 1
            else:
                self.helper(stack)
                p += 1
        
        # print stack, stack[0].getInteger(), stack[0].getList()
        return stack[0]
        
    def helper(self, stack):
        print stack 
        
        lst = []
        elem = stack.pop()
        while elem != '[':
            lst.insert(0, elem)
            elem = stack.pop()
        
        nInteger = NestedInteger()
        
        for elem in lst:
            nInteger.add( (elem if isinstance(elem, NestedInteger) else int(elem)))
        
        stack.append(nInteger)
        
# 2. 用recursive（）。

        # if s == '[]': return NestedInteger()
        # if s[0] != '[':
        #     return NestedInteger(int(s))
        
        # n = NestedInteger()
        
        # p = 1
        # while p < len(s):
        #     if s[p].isdigit() or s[p] == '-':
        #         start = p
                
        #         while p < len(s) and (s[p].isdigit() or s[p] == '-'):
        #             p += 1
                
        #         n.add(int(s[start:p]))
                
        #         p += 1
        #     else:
        #         start = p
        #         count = 1
                
        #         while count > 0:
        #             p += 1
        #             if s[p] == '[':
        #                 count += 1
        #             if s[p] == ']':
        #                 count -= 1
                
        #         p += 1
                
        #         n.add(self.deserialize(s[start:p]))
                
        #         p += 1
        # return n
        
        
        
        