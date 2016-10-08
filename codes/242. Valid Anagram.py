class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mp1 = {}
        mp2 = {}
        
        for c in s:
            mp1[c] =mp1[c] + 1 if c in mp1 else 1
        for c in t:
            mp2[c] = mp2[c] + 1 if c in mp2 else 1
        
        for c in mp1:
            if c not in mp2 or mp1[c] != mp2[c]:
                return False
        for c in mp2:
            if c not in mp1 or mp2[c] != mp1[c]:
                return False
        return True