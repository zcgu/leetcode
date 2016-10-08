# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        a = 0
        b = len(self.lst)   # hou bu hou a
        
        while a < b:
            mid = (a + b) / 2
            
            if self.lst[mid].start == val:
                return
            elif self.lst[mid].start < val:
                a = mid + 1
            else:
                b = mid
        
        self.lst.insert(a, Interval(val, val))
        
        p = max(0, a - 1)
        while p < len(self.lst) - 1 and self.lst[p].end >= self.lst[p+1].start - 1:
            self.lst[p].end = max(self.lst[p].end, self.lst[p+1].end)
            del self.lst[p+1]
        
        p = max(0, a)
        while p < len(self.lst) - 1 and self.lst[p].end >= self.lst[p+1].start - 1:
            self.lst[p].end = max(self.lst[p].end, self.lst[p+1].end)
            del self.lst[p+1]
        
        
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.lst


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()