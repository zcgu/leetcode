class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str = str.lstrip(' ')
        
        if len(str) == 0:
            return 0
            
        f = 1
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            str = str[1:]
            f = -1
        
        res = 0
        i = 0
        while i < len(str) and str[i].isdigit():
            res = res * 10 + f * int(str[i])
            i += 1
            
            if res > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif res < - 2 ** 31:
                return - 2 ** 31
        return res
        