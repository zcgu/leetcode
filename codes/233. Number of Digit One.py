class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        13785 百位-> 137,85 -> 131,##共有(13 + 1) * 100情况
        1. 特殊情况：130，85 -> 131,##就没有了 -> 减去一个100
        2. 特殊情况: 131,85 -> 131,##只有86个 -> 减去一个100， 加一个(85 + 1)
        """
        res = 0
        m = 1
        while m <= n:
            a = n / m
            b = n % m
            
            res += (a / 10 + 1) * m
            
            if a % 10 == 1:
                res = res - m + b + 1
            elif a % 10 == 0:
                res = res - m
            
            m *= 10
            
        return res