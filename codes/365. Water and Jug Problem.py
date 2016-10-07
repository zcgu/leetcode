class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        
        if x + y == z or x == z or y == z:
            return True
        
        commonDivisor = self.getCommonDivisor(x, y)
        
        return z % commonDivisor == 0
        
    def getCommonDivisor(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a



    #     self.visit = set()
    #     return self.dfs(0, 0, x, y, z)
        
    # def dfs(self, a, b, x, y, z):
    #     if (a, b) in self.visit:
    #         return False
        
    #     if a + b == z:
    #         return True
        
    #     self.visit.add((a, b))
        
    #     if self.dfs(0, b, x, y, z) or self.dfs(a, 0, x, y, z):
    #         return True
        
    #     if self.dfs(a, y, x, y, z) or self.dfs(x, b, x, y, z):
    #         return True
        
    #     if self.dfs(a+b - min(a+b, y) , min(a+b, y), x, y, z):
    #         return True
        
    #     if self.dfs(min(a+b, x) ,a+b - min(a+b, x), x, y, z):
    #         return True
        
    #     return False
        
        