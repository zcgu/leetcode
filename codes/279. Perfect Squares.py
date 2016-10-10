class Solution(object):
    dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        
        dp = self.dp
        
        l = len(dp)
        
        if l >= n + 1:
            return dp[n]
        
        while len(dp) < n + 1:
            dp.append(2 ** 31 - 1)
        
        for i in range(l, n + 1):
            for k in range(1, n + 1):
                k2 = k ** 2
                if k2 <= i:
                    dp[i] = min(dp[i], dp[i - k2] + 1)
                elif k2 > i:
                    break
                
        return dp[-1]
