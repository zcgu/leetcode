class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
            
        from heapq import *
        heap = [(matrix[0][0], [0, 0])]
        
        visit = [[False for i in range(len(matrix))] for j in range(len(matrix))]
        
        count = 1
        
        while count != k:
            count += 1
            next = heappop(heap)
            x, y = next[1][0], next[1][1]
            
            if x+1 < len(matrix) and visit[x+1][y] == False:
                visit[x+1][y] = True
                heappush(heap, (matrix[x+1][y], [x+1, y]))
                
            if y+1 < len(matrix) and visit[x][y+1] == False:
                visit[x][y+1] = True
                heappush(heap, (matrix[x][y+1], [x, y+1]))
        
        return heappop(heap)[0]
            
        