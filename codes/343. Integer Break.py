class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp那个n
        
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i-j], j * (i - j))    # don't forget j * (i - j)
        
        return dp[-1]