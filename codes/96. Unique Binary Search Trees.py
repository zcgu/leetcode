class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        
        for i in range(1, n + 1):
            for k in range(1, i + 1):
                dp[i] += dp[k - 1] * dp[i - k]
        
        return dp[-1]