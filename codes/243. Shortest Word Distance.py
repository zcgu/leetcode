# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = words.index(word1)
        p2 = words.index(word2)
        res = 2 ** 31 - 1
        
        while p1 < len(words) and p2 < len(words):
            res = min( res, abs(p2 - p1))
            if p1 < p2:
                p1 += 1
                while p1 < len(words) and words[p1] != word1:
                    p1 += 1
            else:
                p2 += 1
                while p2 < len(words) and words[p2] != word2:
                    p2 += 1
        return res
