class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        count = 0
        res = 0
        
        p1 = 0
        p2 = 0
        
        while p2 < len(s):
            if s[p2] in table:
                table[s[p2]] += 1
                if table[s[p2]] == 2:
                    count += 1
            else:
                table[s[p2]] = 1
            
            p2 += 1
            
            
            while count > 0:
                table[s[p1]] -= 1
                
                if table[s[p1]] == 1:
                    count -= 1
                
                p1 += 1
            
            
            res = max(res, p2 - p1)
        
        return res
                
                
                
                