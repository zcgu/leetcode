class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        for i in range(26):
            table[chr(ord('a') + i)] = 0
            table[chr(ord('A') + i)] = 0

        for c in s:
            table[c] += 1
            
        res = 0
        odd = 0
        for v in table.values():
            if v % 2 == 0:
                res += v
            else:
                if odd == 0:
                    odd = v
                else:
                    res += v - 1
        
        return res + odd
