class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # n & (n-1)的话永远会把n的最后一个1给消除掉
        while n > m:
            n = n & (n - 1)
        return n
