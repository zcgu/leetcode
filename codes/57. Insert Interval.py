# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        
        p = -1
        for i in range(len(intervals)):
            if newInterval.start <= intervals[i].start:
                intervals.insert(i, newInterval)
                p = i
                break
        if p == -1:
            intervals.append(newInterval)
            p = len(intervals) - 1
        
        while p + 1 < len(intervals) and intervals[p+1].start <= newInterval.end:
            newInterval.end = max(newInterval.end, intervals[p+1].end)
            del intervals[p+1]
        
        while p - 1 >= 0 and intervals[p-1].end >= newInterval.start:
            newInterval.start = intervals[p-1].start
            newInterval.end = max(newInterval.end, intervals[p-1].end)
            del intervals[p-1]
            p -= 1
        
        return intervals
        
        
        