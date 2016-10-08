class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        
        for i in range(n-1):
            s = self.nextCount(s)
        
        return s
        
    def nextCount(self, s):
        res = ""
        
        count = 0
        last = ''
        for c in s:
            if c == last:
                count += 1
            else:
                if count > 0:
                    res += str(count) + last
                last = c
                count = 1
        
        if count > 0:
            res += str(count) + last
            
        return res