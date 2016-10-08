class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        
        for i in range(len(s)):
            for p2 in [i+1, i]:
                p1 = i-1
                count = 1
                
                while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                    count += 1
                    p1 -= 1
                    p2 += 1
                
                p1 += 1
                p2 -= 1
                
                if (p2 - p1 + 1) > len(res):
                    res = s[p1:p2+1]
        
        return res
            
            
            
        
        
        
        
        
    # def isPali(self, s):
    #     p1 = 0
    #     p2 = len(s) - 1
        
    #     while p1 < p2:
    #         if s[p1] != s[p2]:
    #             return False
    #     return True
        