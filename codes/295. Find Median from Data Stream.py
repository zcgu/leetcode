from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxq = []
        self.minq = []
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.maxq) != len(self.minq):
            heappush(self.maxq, -heappop(self.minq))
        
        heappush(self.minq, num)
            
        if self.minq and self.maxq and self.minq[0] < -self.maxq[0]:
            heappush(self.minq, -heappop(self.maxq))
            heappush(self.maxq, -heappop(self.minq))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxq) == len(self.minq):
            return (float(-self.maxq[0]) + float(self.minq[0])) / 2
        else:
            return self.minq[0]
        
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()