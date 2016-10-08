class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        tmpx = tmpy = False
        
        lenx = len(matrix)
        leny = len(matrix[0])
        
        if matrix[0][0] == 0:
            tmpx = tmpy = True
        for x in range(lenx):
            if matrix[x][0] == 0:
                tmpx = True
        for y in range(leny):
            if matrix[0][y] == 0:
                tmpy = True
        
        for x in range(1, lenx):
            for y in range(1, leny):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0
        
        for x in range(1, lenx):
            for y in range(1, leny):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0
        
        for x in range(lenx):
            if tmpx:
                matrix[x][0] = 0
                
        for y in range(leny):
            if tmpy:
                matrix[0][y] = 0
        