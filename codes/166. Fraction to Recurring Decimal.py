class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator * denominator < 0: sign = '-'
        else: sign = ''
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        a = sign + str(numerator / denominator)
        
        if numerator % denominator == 0: return a
        
        b = ''
        table = {}
        numerator = numerator % denominator
        i = 0
        
        while numerator != 0:
            if numerator in table:
                index = table[numerator]
                return a + '.' + b[:index] + '(' + b[index:] + ')'
                
            table[numerator] = i
            b += str((numerator * 10) / denominator)
            numerator = numerator * 10 % denominator
            i += 1
        
        return a + '.' + b
        