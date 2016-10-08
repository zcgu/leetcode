class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 1. general dp
        
        dp = [[0 for i in range(n)] for j in range(m)]
        for x in range(m):
            dp[x][0] = 1
        for y in range(n):
            dp[0][y] = 1
        
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
        
        return dp[-1][-1]
        
        # 2. 一维dp
        # dp = [1 for _ in range(n)]
            
        # for i in range(1, m):
        #     newdp = [0 for _ in range(n)]
        #     newdp[0] = 1
        #     for j in range(1, n):
        #         newdp[j] = newdp[j-1] + dp[j]
        #     dp = newdp
        
        # return dp[-1]
        
        
        # 3. 用组合算
        # if m == 1 or n == 1: return 1
        
        # t = m + n - 2   # 一共走多少步
        # d = m - 1       # 多少步向下
        
        # res = 1
        
        # for _ in range(d):
        #     res *= t
        #     t -= 1
        
        # for i in range(1, d + 1):
        #     res /= i
        
        # return res
        