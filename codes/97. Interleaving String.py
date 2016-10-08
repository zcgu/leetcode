class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        
        dp[0][0] = True
        
        for i in range(1, len(s1) + 1):
            dp[i][0] = s1[:i] == s3[:i]
        for j in range(1, len(s2) + 1):
            dp[0][j] = s2[:j] == s3[:j]
            
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = s1[i-1] == s3[i+j-1] and dp[i-1][j] or s2[j-1] == s3[i+j-1] and dp[i][j-1]
        
        return dp[-1][-1]
        
        
        