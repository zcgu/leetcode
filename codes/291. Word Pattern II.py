# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Examples:
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.


class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        return self.dfs(pattern, str, {})
    
    def dfs(self, pattern, str, table):
        
        if not pattern:
            return str == ''
        if not str:
            return False
        
        if pattern[0] in table:
            word = table[pattern[0]]
            return str[:len(word)] == word and\
                self.dfs(pattern[1:], str[len(word):], table)
        
        for i in range(1, len(str) + 1):
            if str[:i] in table.values():
                continue
            
            table[pattern[0]] = str[:i]
            if self.dfs(pattern[1:], str[i:], table):
                return True
            del table[pattern[0]]
        
        return False

