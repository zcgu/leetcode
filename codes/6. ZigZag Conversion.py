class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
            
        lst = []
        x = y = 0
        
        down = True
        
        for c in s:
            
            lst.append([x, y, c])
            
            if down:
                if x == numRows - 1:
                    x -= 1
                    y += 1
                    down = False
                else:
                    x += 1
            else:
                if x == 0:
                    x += 1
                    down = True
                else:
                    x -= 1
                    y += 1
        
        res = ""
        
        lst.sort(key=lambda l: l[0] * len(s) + l[1])
        
        for l in lst:
            res += l[2]
            
        return res
        
        