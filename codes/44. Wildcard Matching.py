class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not s:
            for c in p:
                if c != '*':
                    return False
            return True
        if not p:
            for c in s:
                if c != '*':
                    return False
            return True
        
        # c1 = s[0]
        # c2 = p[0]
        
        # if c1 == '*':
        #     for i in range(len(p) + 1):
        #         if self.isMatch(s[1:], p[i:]):
        #             return True
        #     return False
        # elif c2 == '*':
        #     for i in range(len(s) + 1):
        #         if self.isMatch(s[i:], p[1:]):
        #             return True
        #     return False
        # elif c1 == '?' or c2 == '?':
        #     return self.isMatch(s[1:], p[1:])
        # else:
        #     if c1 != c2:
        #         return False
        #     else:
        #         return self.isMatch(s[1:], p[1:])
                
                
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        
        dp[0][0] = True
        
        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j-1] and p[j-1] == '*'
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
                # print dp
        
        return dp[-1][-1]