class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        
        dp = [2 ** 31 - 1 for _ in range(n + 1)]
        dp[0] = 0
        
        for i in range(1, n + 1):
            for k in range(1, n + 1):
                if k * k <= i:
                    dp[i] = min(dp[i], dp[i - k*k] + 1)
                elif k * k > i:
                    break
                
        return dp[-1]