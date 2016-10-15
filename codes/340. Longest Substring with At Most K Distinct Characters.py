# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# For example, Given s = “eceba” and k = 2,

# T is "ece" which its length is 3.

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        p1 = p2 = res =0
        table = {}

        while p2 < len(s):
            table[s[p2]] = table.get(s[p2], 0) + 1
            p2 += 1

            while sum(1 if i > 0 else 0 for i in table.values()) > k:
                table[s[p1]] -= 1
                p1 += 1

            res = max(res, p2 - p1)
        
        return res      
