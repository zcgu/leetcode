class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # 这个边界要先处理，不能加一排空的。
        if not dungeon:
            return 0
            
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[-1][-1] = max(1, - dungeon[-1][-1] + 1)
        
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(1, - dungeon[i][-1] + dp[i+1][-1])
        
        for j in range(n - 2, -1, -1):
            dp[-1][j] = max(1, - dungeon[-1][j] + dp[-1][j+1])
            
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, - dungeon[i][j] + min(dp[i+1][j], dp[i][j+1]))
        
        return dp[0][0]
    