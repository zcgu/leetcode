class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in ransomNote:
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True