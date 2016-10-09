class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        
        m = self.m = len(matrix)
        n = self.n = len(matrix[0])

        can1 = set()
        can2 = set()
        visited1 = set()
        visited2 = set()
        
        for x in range(m):
            self.dfs(matrix, x, 0, can1, visited1)
            self.dfs(matrix, x, n - 1, can2, visited2)
        for y in range(n):
            self.dfs(matrix, 0, y, can1, visited1)
            self.dfs(matrix, m - 1, y, can2, visited2)
        
        res = set()
        for pair in can1:
            if pair in can2:
                res.add(pair)
        return list(res)
        
        
    def dfs(self, matrix, x, y, can, visited):
        can.add((x, y ))
        visited.add((x, y))
        
        for xx, yy in [(x + 1, y), ( x - 1, y), ( x, y + 1), (x, y - 1)]:
            if xx >= 0 and xx < self.m and yy >= 0 and yy < self.n and matrix[xx][yy] >= matrix[x][y] and \
                (xx, yy ) not in visited:
                    self.dfs(matrix, xx, yy, can, visited)
                    
        


                
        # from heapq import *
        # heap = []
        
        # can1 = set()
        # can2 = set()
        
        # visit = set()
        
        # for i in range(m):
        #     heappush(heap, (matrix[i][0], [i, 0, 1]))
        #     visit.add((i, 0, 1))
        #     heappush(heap,(matrix[i][n - 1], [i,  n - 1, 2]))
        #     visit.add((i, n - 1, 2))
        # for j in range(n):
        #     heappush(heap,(matrix[0][j], [0, j, 1]))
        #     visit.add((0, j, 1))
        #     heappush(heap,(matrix[m - 1][j], [m - 1,  j, 2]))
        #     visit.add((m - 1, j, 2))
        
        # while heap:
        #     h, index = heappop(heap)
        #     x = index[0]
        #     y = index[1]
        #     c = index[2]
            
        #     if c == 1: can1.add((x, y))
        #     else: can2.add((x, y))
            
        #     for xx, yy in [(x+1, y), (x-1,y), (x, y+1), (x,y -1)]:
        #         if xx >= 0 and xx < m and yy >=0 and yy < n and matrix[xx][yy] >= h and (xx, yy, c) not in visit:
        #             heappush(heap, (matrix[xx][yy], [xx, yy, c]))
        #             visit.add((xx, yy, c))
        
        # res = []
        # for pos in can1:
        #     if pos in can2:
        #         res.append(pos)
        # return res
            
            
            
            
            
            
        
        
