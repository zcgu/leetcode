class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        
        dp = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]
        
        dp[0][0] = triangle[0][0]
        
        for lvl in range(1, len(triangle)):
            dp[lvl][0] = dp[lvl-1][0] + triangle[lvl][0]
            dp[lvl][-1] = dp[lvl-1][-1] + triangle[lvl][-1]
            
            for i in range(1, len(triangle[lvl]) - 1):
                dp[lvl][i] = min(dp[lvl-1][i-1], dp[lvl-1][i]) + triangle[lvl][i]
        
        return min(dp[-1])
        