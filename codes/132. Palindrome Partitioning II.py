class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这题巧妙，对每个位置i，找到最大的pali长度j，更新dp[i+j]，注意多种情况。
        
        if not s:
            return 0
            
        dp = [0 for _ in range(len(s) + 1)]
        
        for i in range(len(s) + 1):         # 第一项是-1,因为1+dp[0]就是不分割，正好是0.
            dp[i] = i - 1
        
        for i in range(len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i-j] == s[i+j]:
                dp[i+j+1] = min(dp[i+j+1], 1 + dp[i-j -1 +1])           # 这个放在循环里面，比较简洁，注意i-j-1+1
                j += 1
            
            j = 0
            while i - j >= 0 and i + j + 1 < len(s) and s[i-j] == s[i+j+1]:
                dp[i+j+2] = min(dp[i+j+2], 1 + dp[i-j -1 +1])
                j += 1
            
        return dp[-1]