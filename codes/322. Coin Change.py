class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp amount。
        
        dp = [2 ** 31 - 1 for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        
        return dp[-1] if dp[-1] != 2 ** 31 - 1 else -1
        
        
        # 第二种，dfs
        
    #     coins.sort()
    #     return self.dfs(coins, amount)
            
    # def dfs(self, coins, num):
    #     if num < 0:
    #         return -1
    #     if num == 0:
    #         return 0
            
    #     for coin in reversed(coins):

    #         res = self.dfs(coins, num - coin)
            
    #         if res != -1:
    #             return 1 + res
        
    #     return -1