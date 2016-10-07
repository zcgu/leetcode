class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return 10
        # if n == 2:
        #     return 91
        
        
        # lst = [0, 10, 81]
        
        # for i in range(3, n+1):
        #     lst.append(lst[-1] * max(0, (10 - (i - 1))) )
        
        # return sum(lst)
        
        
        # 2. 这个易于理解
        if n == 0: return 1
        
        res = 0
        
        for i in range(1, n + 1):
            res += self.countOneCase(i)
        
        return res
            
            
            
    def countOneCase(self, n):
        # 9 * 9 * 8 * 7 * 6

        if n > 10: return 0
        if n == 1: return 10
        
        res = 9
        for i in range(1, n):
            res *= (10 - i)
        return res
        
        

