class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        table = {1:'I', 4:'VI', 5:'V', 9:'XI', 10:'X', 40:'LX', 50:'L',\
            90:'CX', 100:'C', 400:'DC', 500:'D', 900:'MC', 1000:'M'}
            
        res = ''
        
        while num > 0:
            for v in reversed(sorted(table.keys())):
                if num >= v:
                    res = table[v] + res
                    num -= v
                    break
        
        return res[::-1]