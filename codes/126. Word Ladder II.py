class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :rtype: List[List[int]]
        :type wordlist: Set[str]
        """
        if beginWord == endWord:
            return [[endWord]]
            
        if not wordList:
            return False
        
        wordList.discard(beginWord)
        wordList.add(endWord)
        
        lst = [beginWord]
        self.mp = {}
        self.res = []
        
        while endWord in wordList:
            lst = self.nextLst(lst, wordList)
            
            if not lst:
                return []
                
        self.output(endWord, [endWord])
        
        return self.res
        
    
    def nextLst(self, lst, dic):
        res = []
        
        for word in lst:
            for i in range(len(word)):
                for j in range(26):
                    c = chr(ord('a') + j)
                    
                    if c == word[i]:
                        continue
                    
                    newword = word[:i] + c + word[i+1:]
                    if newword in dic:
                        self.mp[newword] = self.mp[newword] + [word] if newword in self.mp else [word]
                        
                        if newword not in res:
                            res.append(newword)
        
        for word in res:
            dic.remove(word)
        
        return res
            
    def output(self, word, lst):
        if word not in self.mp:
            self.res.append(lst)
            return
        
        for parent in self.mp[word]:
            self.output(parent, [parent] + lst)
            
            
        
        
        
        
        
        
        
        
        
        