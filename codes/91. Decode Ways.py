class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        dp = [0 for _ in range(len(s))]
        dp[0] = 1 if '1' <= s[0] <= '9' else 0
        
        for i in range(1, len(s)):
            if '1' <= s[i] <= '9':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1

        return dp[-1]
        

    #     if not s:
    #         return 0
            
    #     self.res = 0
    #     self.dfs(s)
    #     return self.res
    
    # def dfs(self, s):
    #     if not s:
    #         self.res += 1
    #         return
        
    #     if s[0] == '0':
    #         return
        
    #     self.dfs(s[1:])
        
    #     if 10 <= int(s[:2]) <= 26:
    #         self.dfs(s[2:])
            
            
            