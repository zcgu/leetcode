class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 这个题，我觉着dp就够好了。
        
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
                
        # dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        
        # dp[0][0] = True
        
        # for j in range(1, len(p) + 1):
        #     dp[0][j] = dp[0][j-1] and p[j-1] == '*'
        
        # for i in range(1, len(s) + 1):
        #     for j in range(1, len(p) + 1):
        #         if p[j-1] == '*':
        #             dp[i][j] = dp[i][j-1] or dp[i-1][j]
        #         elif p[j-1] == '?':
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        #         # print dp
        
        # return dp[-1][-1]
        
        
        
        
        lst = p.split('*')
        lst = [l for l in lst if l != '']

        p1 = p2 = 0

        if p[0] != '*' and not self.equals(s, lst, 0, 0): return False
        if p[-1] != '*' and not self.equals(s, lst, len(s) - len(lst[-1]), len(lst) - 1):
            return False
        if p[0] != '*' and p[-1] != '*' and len(lst) == 1:
            return len(p) == len(s) and self.equals(s, lst, 0, 0)
            
        while p1 < len(s) and p2 < len(lst):
            if self.equals(s, lst, p1, p2):
                p1 += len(lst[p2])
                p2 += 1
            else:
                p1 += 1

        return p2 == len(lst)

    def equals(self, s, lst, p1, p2):
        tmp = s[p1:p1 + len(lst[p2])]
        if len(tmp) != len(lst[p2]): return False

        for i in range(len(tmp)):
            if lst[p2][i] != '?' and tmp[i] != lst[p2][i]:
                return False

        return True
        



