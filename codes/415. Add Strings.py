class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        carry = 0
        
        p1 = len(num1) -1
        p2 = len(num2) - 1
        
        while p1 >= 0 or p2 >= 0:
            tmp = carry
            if p1 >= 0:
                tmp += ord(num1[p1]) - ord('0')
                p1 -= 1
            if p2 >= 0:
                tmp += ord(num2[p2]) - ord('0')
                p2 -= 1
            res = str(tmp % 10) + res
            carry = tmp / 10
        
        if carry != 0:
            res = str(carry) + res
            
        return res
