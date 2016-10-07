class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        res = 1
        absn = abs(n)
        
        while absn > 0:
            if (absn & 1 == 1):
                res *= x
            absn = absn >> 1
            x *= x
        
        return res if n > 0 else 1 / res
        