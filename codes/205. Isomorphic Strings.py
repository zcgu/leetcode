class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        map = {}
        map2 = {}
        
        for i in range(len(s)):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            else:
                if t[i] in map2:
                    return False
                map[s[i]] = t[i]
                map2[t[i]] = s[i]
        
        return True