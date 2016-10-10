# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# word1 and word2 may be the same and they represent two individual words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = "makes", word2 = "makes", return 3.

# Note:
# You may assume word1 and word2 are both in the list.

# Show Company Tags
# Show Tags
# Show Similar Problems

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = words.index(word1)
        
        if word1 != word2:
            p2 = words.index(word2)
        else:
            p2 = p1 + 1
            while p2 < len(words) and words[p2] != word2:
                p2 += 1
                    
        res = 2 ** 31 - 1
        
        while p1 < len(words) and p2 < len(words):
            res = min( res, abs(p2 - p1))
            if p1 < p2:
                if word1 == word2:
                    p1 = p2 + 1
                else:
                    p1 += 1
                    
                while p1 < len(words) and words[p1] != word1:
                    p1 += 1
            else:
                if word1 == word2:
                    p2 = p1 + 1
                else:
                    p2 += 1
                    
                while p2 < len(words) and words[p2] != word2:
                    p2 += 1
        return res
