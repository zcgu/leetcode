class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        rowh = [0 for _ in range(n)]
        res = 0

        for x in range(m):
            for y in range(n):
                rowh[y] = 0 if matrix[x][y] == '0' else rowh[y] + 1
            
            res = max(res, self.findMaxArea(rowh))
            
        return res
        
    def findMaxArea(self, hs):
        hs = hs + [0]
        stack = []
        res = 0
        for i in range(len(hs)):
            while stack and hs[i] < hs[stack[-1]]:
                lasth = hs[stack.pop()]
                
                left = -1 if not stack else stack[-1]
                
                res = max(res, lasth * ( i - (left + 1)))
                
            stack.append(i)
            
        return res