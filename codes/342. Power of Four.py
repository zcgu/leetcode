class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 : return False
        
        # 0101 0101 0101
        return 0x55555555 | num == 0x55555555 and (num - 1) & num == 0
