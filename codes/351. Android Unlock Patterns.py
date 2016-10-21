class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [[False for _ in range(3)] for _ in range(3)]
        
        res = 0
        for i in range(m, n + 1):
            res += self.dfs(i, visited, -1, -1)
            
        return res
        
    def dfs(self, n, visited, lastx, lasty):
        if n == 0: return 1
        
        res = 0
        for x in range(3):
            for y in range(3):
                if visited[x][y]: continue
                
                if lastx > -1 and x == lastx and abs(y - lasty) == 2 and not visited[x][1]:
                    continue
                
                if lastx > -1 and y == lasty and abs(x - lastx) == 2 and not visited[1][y]:
                    continue
                
                if lastx > -1 and abs(x - lastx) == 2 and abs(y - lasty) == 2 and not visited[1][1]:
                    continue
                
                visited[x][y] = True
                
                res += self.dfs(n - 1, visited, x, y)
                
                visited[x][y] = False
        return res
                
