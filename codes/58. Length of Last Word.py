class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ')
        lst = s.split()
        if not lst:
            return 0
        else:
            return len(lst[-1])