class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
            
        self.cache = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        self.res = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                self.res = max(self.res, self.dfs(matrix, x, y))
        return self.res
        
    def dfs(self, m, x, y):
        if self.cache[x][y] != -1:
            return self.cache[x][y]
        
        res = 1
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if x + i >= 0 and x + i < len(m) and y + j >= 0 and y + j < len(m[0]) \
                and m[x + i][y + j] > m[x][y]:
                    res = max(res, 1 + self.dfs(m, x + i, y + j))
        
        self.cache[x][y] = res
        return res
        