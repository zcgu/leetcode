class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        
        if num == 1:
            return True
        
        while num != 1:
            if num % 4 != 0:
                return False
            num /= 4
        
        return True