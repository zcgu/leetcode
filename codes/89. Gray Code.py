class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        lst = ["0", "1"]
        
        for turn in range(2, n+1):
            lst2 = lst[:]
            lst2.reverse()
            lst += lst2
            
            for i in range(len(lst)/2):
                lst[i] = "0" + lst[i]
            for i in range(len(lst)/2, len(lst)):
                lst[i] = "1" + lst[i]
        
        res = []
        for l in lst:
            res.append(self.toInt(l))
        return res
        
    
    def toInt(self, s):
        res = 0
        for c in s:
            res = 2 * res + int(c)
        return res