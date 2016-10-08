class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mp = {}
        
        for c in s:
            mp[c] = mp[c] + 1 if c in mp else 1
        
        for i, c in enumerate(s):
            if mp[c] == 1:
                return i
        
        return -1