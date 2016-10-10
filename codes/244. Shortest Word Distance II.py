# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        table = self.table = {}
        
        for i, word in enumerate(words):
            table[word] = table[word] + [i] if word in table else [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = 0
        p2 = 0
        
        res = 2 ** 31 - 1
        
        lst1 = self.table[word1]
        lst2 = self.table[word2]
        
        while p1 < len(lst1) and p2 < len(lst2):
            res = min(res, abs(lst1[p1] - lst2[p2]))
            
            if lst1[p1] < lst2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        return res
        

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
