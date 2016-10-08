class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
        
        visit = [ [False for _ in range(n)] for _ in range(m)]
        
        x = y = 0
        dx = 0
        dy = 1
        
        while 0 <= x < m and 0 <= y < n and not visit[x][y]:    # judgement don't forget
            
            res.append(matrix[x][y])
            visit[x][y] = True
            
            xx = x + dx
            yy = y + dy
            if xx < 0 or xx >= m or yy < 0 or yy >= n or visit[xx][yy]:
                if dx == 0 and dy == 1:
                    dx = 1
                    dy = 0
                elif dx == 1 and dy == 0:
                    dx = 0
                    dy = -1
                elif dx == 0 and dy == -1:
                    dx = -1
                    dy = 0
                else:
                    dx = 0
                    dy = 1
            
            
            x += dx
            y += dy
        
        return res
            