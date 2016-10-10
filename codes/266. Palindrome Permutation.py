# Given a string, determine if a permutation of the string could form a palindrome.

# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hasOdd = False
        
        for c in set(s):
            if s.count(c) % 2 != 0:
                if hasOdd:
                    return False
                else:
                    hasOdd = True
        return True
