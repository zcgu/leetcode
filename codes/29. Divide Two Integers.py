class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0:
            negetive = False
        else:
            negetive = True
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        
        f = 1
        
        d2 = divisor
        
        while dividend >= d2:
            d2 = d2 << 1
            f *= 2
        
        while dividend >= divisor:
            if dividend >= d2:
                dividend -= d2
                res += f

            if f > 1:
                d2 = d2 >> 1
                f /= 2
        
        res = -res if negetive else res
        
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < - 2 ** 31:
            return - 2 ** 31
        return res
            
            
            
            
            
            
            