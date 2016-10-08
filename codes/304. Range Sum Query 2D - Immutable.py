class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.dp = None
            return
            
        m = len(matrix)
        n = len(matrix[0])
        
        dp = self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for x in range(1, m + 1):   # 0 的都是零就不用单独处理了。
            for y in range(1, n + 1):
                dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] + matrix[x-1][y-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.dp:
            return 0
            
        row1 -= 1
        col1 -= 1
        
        dp = self.dp
        
        return dp[row2 + 1][col2 + 1] - dp[row1 +1][col2 + 1] - dp[row2 + 1][col1 + 1] + dp[row1 + 1][col1 + 1]
        
        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)