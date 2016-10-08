class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
            
        wordList.add(endWord)
        
        lst = [beginWord]
        
        cur = 1
        
        while lst:
            lst = self.getNext(lst, wordList)
            cur += 1
            
            if endWord not in wordList:
                return cur
        return 0
        
    def getNext(self, lst, wordList):
        tmp = []
        
        for s in lst:
            for i in range(len(s)):
                for j in range(26):
                    c = chr(ord('a') + j)
                    if c == s[i]:
                        continue
                    s2 = s[:i] + c + s[i+1:]
                    if s2 in wordList:
                        tmp.append(s2)
                        wordList.remove(s2)
        return tmp