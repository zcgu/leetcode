class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # while num >= 10:
        #     tmp = 0
        #     while num != 0:
        #         tmp += num % 10
        #         num /= 10
        #     num = tmp
        
        # return num
        
        # 36,9 37,10,1 38,11,2 39,12,3 40,4 41,5 
        
        if num == 0:
            return 0
        
        if num % 9 == 0:
            return 9
        
        return num % 9