class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # (n - 1) & n == 0 判断2的pow，也就是只有1个1的方式
        
        if n <= 0: return False
        # return (2 ** 50) % n == 0
        return (n - 1) & n == 0
        
        # if n == 0:
        #     return False
        
        # if n == 1:
        #     return True
            
        # while n != 1:
        #     if n % 2 != 0:
        #         return False
        #     n /= 2
        
        # return True
