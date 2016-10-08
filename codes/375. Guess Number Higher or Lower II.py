class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[start][end],先遍历区间长度。
        
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]  # 这个n＋2是为了下边的卡k－1和k＋1，k－1和k＋1能大于end的。
        
        for length in range(1, n+1):
            for start in range(1, n+1):
                if start + length > n:
                    continue
                
                end = start + length
                dp[start][end] = 2 ** 31 - 1
                
                for k in range(start, end + 1):
                    dp[start][end] = min(dp[start][end], k + max(dp[start][k-1], dp[k+1][end]))
        
        return dp[1][n]