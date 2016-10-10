# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

# Show Company Tags
# Show Tags
# Show Similar Problems


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        lst = []
        
        for i in intervals:
            lst.append([i.start, 1])
            lst.append([i.end, -1])
        
        lst.sort(key=lambda l: [l[0], l[1]])
        
        count = 0
        res = 0
        for time, sign in lst:
            count += sign
            res = max(res, count)
        
        return res
