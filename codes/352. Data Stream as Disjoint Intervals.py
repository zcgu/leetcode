# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class MyNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self.root:
            self.root = MyNode(val)
            return
        
        self.add(self.root, val)
        
    def add(self, t,val):
        if t.val == val:
            return
        
        elif val < t.val:
            if t.left:
                return self.add(t.left, val)
            else:
                node = MyNode(val)
                t.left = node
                return
        else:
            if t.right:
                return self.add(t.right, val)
            else:
                node = MyNode(val)
                t.right = node
                return
            

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        self.res = []
        self.inorder(self.root)
        return self.res
        
    def inorder(self, node):
        if not node:
            return
        
        self.inorder(node.left)
        
        if not self.res or node.val > self.res[-1].end + 1:
            i = Interval(node.val, node.val)
            self.res.append(i)
        else:
            self.res[-1].end = node.val
        
        self.inorder(node.right)


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

# # Definition for an interval.
# # class Interval(object):
# #     def __init__(self, s=0, e=0):
# #         self.start = s
# #         self.end = e

# class SummaryRanges(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.lst = []
        

#     def addNum(self, val):
#         """
#         :type val: int
#         :rtype: void
#         """
#         a = 0
#         b = len(self.lst)   # hou bu hou a
        
#         while a < b:
#             mid = (a + b) / 2
            
#             if self.lst[mid].start == val:
#                 return
#             elif self.lst[mid].start < val:
#                 a = mid + 1
#             else:
#                 b = mid
        
#         self.lst.insert(a, Interval(val, val))
        
#         p = max(0, a - 1)
#         while p < len(self.lst) - 1 and self.lst[p].end >= self.lst[p+1].start - 1:
#             self.lst[p].end = max(self.lst[p].end, self.lst[p+1].end)
#             del self.lst[p+1]
        
#         p = max(0, a)
#         while p < len(self.lst) - 1 and self.lst[p].end >= self.lst[p+1].start - 1:
#             self.lst[p].end = max(self.lst[p].end, self.lst[p+1].end)
#             del self.lst[p+1]
        
        
        

#     def getIntervals(self):
#         """
#         :rtype: List[Interval]
#         """
#         return self.lst


# # Your SummaryRanges object will be instantiated and called as such:
# # obj = SummaryRanges()
# # obj.addNum(val)
# # param_2 = obj.getIntervals()
