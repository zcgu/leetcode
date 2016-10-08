class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        res = m
        for i in range(m+1, n+1):
            res &= i
        return res