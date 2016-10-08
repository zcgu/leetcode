class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ob = obstacleGrid
        if not ob:
            return 0
            
        dp = [[0 for j in range(len(ob[0]))] for i in range(len(ob))]
        dp[0][0] = 1 if ob[0][0] == 0 else 0
        
        for i in range(1, len(ob)):
            if ob[i][0] == 0 and dp[i-1][0] > 0:
                dp[i][0] = 1
        
        for j in range(1, len(ob[0])):
            if ob[0][j] == 0 and dp[0][j-1] > 0:
                dp[0][j] = 1
        
        for i in range(1, len(ob)):
            for j in range(1, len(ob[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if ob[i][j] == 0 else 0
        
        return dp[-1][-1]
        