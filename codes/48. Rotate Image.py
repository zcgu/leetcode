class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for x in range(n):
            for y in range(x, n):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
                
        for x in range(n):
            for y in range(n/2):
                matrix[x][y], matrix[x][n-y-1] = matrix[x][n-y-1], matrix[x][y]
        
        return