class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        
        while l < r:
            mid = (l + r) / 2 + 1
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid
            else:
                r = mid - 1
        return l