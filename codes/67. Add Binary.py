class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        
        carry = 0
        
        p1 = len(a) - 1
        p2 = len(b) - 1
        
        while p1 >= 0 or p2 >= 0:
            tmp = carry
            
            if p1 >= 0:
                tmp += int(a[p1])
                p1 -= 1
            if p2 >= 0:
                tmp += int(b[p2])
                p2 -= 1
                
            res = str(tmp % 2) + res
            carry = tmp / 2
        
        if carry == 1:
            res = '1' + res
        
        return res
            
            