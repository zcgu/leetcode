class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        
        i = 1
        x = y = 0
        dx = 0
        dy = 1
        while i <= n * n:
            print x, y
            res[x][y] = i
            i += 1
            
            if x + dx < 0 or x + dx >= n or y + dy < 0 or \
                y + dy >= n or res[x+dx][y+dy] != 0:
                    if dx == 0 and dy == 1:
                        dx, dy = 1, 0
                    elif dx == 1 and dy == 0:
                        dx, dy = 0, -1
                    elif dx == 0 and dy == -1:
                        dx, dy = -1, 0
                    else:
                        dx, dy = 0, 1
            
            x += dx
            y += dy
            
        return res