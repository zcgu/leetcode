class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1. loop 做法
        
        # if n == 0:
        #     return False
        # if n == 1:
        #     return True
        # while n != 1:
        #     if n % 3 != 0:
        #         return False
        #     else:
        #         n /= 3
        # return True
        
        # 2. 一行做法
        if n <= 0: return False
        
        return (3 ** 50) % n == 0
