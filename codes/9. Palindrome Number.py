class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
            
        x2 = x
        
        r = 0
        
        while x2 != 0:
            r = r * 10 + x2 % 10
            x2 /= 10
        
        return r == x

        # 2. 这个处理了overflow。
        
        # if x < 0:
        #     return False
        
        # if x != 0 and x % 10 == 0:
        #     return False
        
        # n = 0
        # while x > n:
        #     n = n*10 + x%10
        #     x /= 10
        # return x == n or x == n/10