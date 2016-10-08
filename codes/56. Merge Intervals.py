# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda l: l.start)
        
        p = 0
        while p < len(intervals) - 1:
            if intervals[p+1].start <= intervals[p].end:
                intervals[p].end = max(intervals[p].end, intervals[p+1].end)
                del intervals[p+1]
            else:
                p += 1
        return intervals