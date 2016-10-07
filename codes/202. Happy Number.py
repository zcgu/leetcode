class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()
        
        while n != 1:
            if n in visit: return False
            visit.add(n)
            
            n2 = 0
            while n != 0:
                n2 += (n % 10) ** 2
                n /= 10
            
            n = n2
        
        return True
            