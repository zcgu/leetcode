# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        
        while l < h:
            mid = (l + h) / 2
            
            if isBadVersion(mid):
                h = mid
            else:
                l = mid + 1
        
        return l