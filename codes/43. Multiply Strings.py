class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        lst = [0 for _ in range(len(num1) + len(num2) + 1)]
        
        for i1, n1 in enumerate(reversed(list(num1))):
            for i2, n2 in enumerate(reversed(list(num2))):
                lst[i1 + i2] += int(n1) * int(n2)           # important part
        
        res = ''
        a = 0
        for i in range(len(lst)):
            tmp = lst[i] + a
            res = str(tmp % 10) + res
            a = tmp / 10
        if a > 0:
            res = str(a) + res
        
        res = res.lstrip('0')
        
        return res if res else '0'
        
        

        
    #     res = ''
    #     f = 0
    #     for c in reversed(num2):
    #         tmp = self.multiOne(num1, c) + '0' * f
    #         f += 1
    #         res = self.addTwo(res, tmp)
    #     return res[:-1].lstrip('0') + res[-1]
        
    # def multiOne(self, num, n):
    #     res = ''
        
    #     a = 0
    #     for c in reversed(num):
    #         tmp = a + int(c) * int(n)
    #         res = str(tmp % 10) + res
    #         a = tmp / 10
        
    #     if a > 0:
    #         res = str(a) + res
        
    #     return res
    
    # def addTwo(self, num1, num2):
    #     res = ''
        
    #     a = 0
        
    #     p1 = len(num1) - 1
    #     p2 = len(num2) - 1
        
    #     while p1 >=0 or p2 >= 0:
    #         n1 = int(num1[p1]) if p1 >= 0 else 0
    #         n2 = int(num2[p2]) if p2 >= 0 else 0
            
    #         tmp = n1 + n2 + a
            
    #         res = str(tmp % 10) + res
    #         a = tmp / 10
            
    #         p1 -= 1
    #         p2 -= 1
        
    #     if a > 0:
    #         res = str(a) + res
        
    #     return res
        
        
        
        