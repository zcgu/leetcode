class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        
        x2 = x
        
        r = 0
        
        while x2 != 0:
            r = r * 10 + x2 % 10
            x2 /= 10
        
        r = r * sign
        
        if r > 2 ** 31 - 1:
            return 0
        elif r < - 2 ** 31:
            return 0
        else:
            return r