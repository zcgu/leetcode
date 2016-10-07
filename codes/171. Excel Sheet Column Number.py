class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        f = 1
        res = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            res += f * (ord(c) - ord('A') + 1)
            f *= 26
        return res