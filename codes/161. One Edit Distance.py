# Given two strings S and T, determine if they are both one edit distance apart.

# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == t: return False
        
        if len(s) == len(t):
            for i in range(len(s) + 1):
                if s[:i] + s[i+1:] == t[:i] + t[i+1:]:
                    return True
        
        for i in range(len(s) + 1):
            if s[:i] + s[i+1:] == t:
                return True
        
        for i in range(len(t) + 1):
            if s == t[:i] + t[i+1:]:
                return True
        
        return False
        
