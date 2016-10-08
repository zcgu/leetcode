class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
            
        from heapq import *
        
        hp = []
        
        mp = heightMap
        
        m = len(mp)
        n = len(mp[0])
        
        visit = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            if not visit[i][0]:
                heappush(hp, (mp[i][0], [i, 0]))
                visit[i][0] = True
            if not visit[i][n-1]:
                heappush(hp, (mp[i][n-1], [i, n-1]))
                visit[i][n-1] = True
        for j in range(n):
            if not visit[0][j]:
                heappush(hp, (mp[0][j], [0, j]))
                visit[0][j] = True
                 
            if not visit[m-1][j]:
                heappush(hp, (mp[m-1][j], [m-1, j]))
                visit[m-1][j] = True
        
        res = 0
        while hp:
            pair = heappop(hp)
            pairh = pair[0]
            x, y = pair[1]
            
            for xx, yy in [(x+1,y), (x-1, y), (x,y+1), (x,y-1)]:
                if xx > 0 and xx < m-1 and yy > 0 and yy < n -1 and not visit[xx][yy]:
                    visit[xx][yy] = True
                    
                    if mp[xx][yy] < pairh:
                        res += pairh - mp[xx][yy]
                    
                    heappush(hp, (max(mp[xx][yy], pairh), [xx, yy]))
        
        return res
            
        
        