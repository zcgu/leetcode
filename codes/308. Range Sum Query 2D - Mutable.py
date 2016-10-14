# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# Show Company Tags
# Show Tags
# Show Similar Problems


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix: 
            self.matrix = None
            return 
    
        m = len(matrix)
        n = len(matrix[0])

        self.matrix = [[0 for _ in range(n)] 
                        for _ in range(m)]
        self.tree = [[0 for _ in range(n + 1)]
                        for _ in range(m + 1)]
        for x in range(m):
            for y in range(n):
                self.update(x, y, matrix[x][y])
            

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if not self.matrix: return
    
        m = len(self.matrix)
        n = len(self.matrix[0])

        i = row + 1
        
        while i < m + 1:
            j = col + 1
            while j < n + 1:
                self.tree[i][j] += val - self.matrix[row][col]
                j += j & -j
            i += i & -i
        
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix: return 0
        
        return self.sumCorner(row2, col2)\
                - self.sumCorner(row1 - 1, col2)\
                - self.sumCorner(row2, col1 - 1)\
                + self.sumCorner(row1 - 1, col1 - 1)

    def sumCorner(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return res

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)


