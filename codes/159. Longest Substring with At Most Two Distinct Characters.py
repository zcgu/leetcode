# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

# For example, Given s = “eceba”,

# T is "ece" which its length is 3.

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        table = {}
        count = 0
        res = 0
        
        p1 = p2 = 0
        
        while p2 < len(s):
            table[s[p2]] = table[s[p2]] + 1 if s[p2] in table else 1
            if table[s[p2]] == 1: count += 1
            p2 += 1
            
            while count > 2:
                table[s[p1]] -= 1
                if table[s[p1]] == 0: count -= 1
                p1 += 1
            
            res = max(res, p2 - p1)
        
        return res
            
