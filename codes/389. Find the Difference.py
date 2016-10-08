class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # l1 = list(s)
        # l2 = list(t)
        
        # l1.sort()
        # l2.sort()
        
        # for i in range(len(s)):
        #     if l1[i] != l2[i]:
        #         return l2[i]
        # return l2[-1]
        
        c = 0
        for i in s + t:
            c ^= ord(i)
        return chr(c)
        