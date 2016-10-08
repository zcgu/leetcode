class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        res = 0
        for x in range(m):
            for y in range(n):
                dp[x+1][y+1] = 0 if matrix[x][y] == '0' else 1 + min(dp[x][y] , dp[x+1][y], dp[x][y+1])
                res = max(res, dp[x+1][y+1] ** 2)
        
        return res