# Write a function to generate the generalized abbreviations of a word.

# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """

        return self.dfs(word)

    def dfs(self, word):
        if not word: return ['']

        res = []
        res += [word[0] + s for s in self.dfs(word[1:])]

        for i in range(1, len(word)):
            res += [str(i) + word[i] + s for s in self.dfs(word[i+1:])]

        res += [str(len(word))]

        return res


