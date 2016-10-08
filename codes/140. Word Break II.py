class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        
        
        # 1. dp 版本，并不能过。
        
        # dp = [set() for i in range(len(s) + 1)]
        
        # for i in range(len(s) + 1):
        #     if s[:i] in wordDict:
        #         dp[i].add(s[:i])
            
        #     for word in wordDict:
        #         if s[i:i + len(word)] == word and i + len(word) <= len(s):
        #             for sentence in dp[i]:
        #                 dp[i + len(word)].add(sentence + ' ' + word)
        
        # return list(dp[-1])


        # 2. 带memery的dfs，mem 是memorize，这个可以过。

        return self.nextWord(s, {}, wordDict)
        
    def nextWord(self, s, mem, dict):
        if not s: return [None]
                                                # 这里千万不能加if s in dic: return [s]
        if s in mem: return mem[s]
        
        res = []
        for word in dict:
            if s[:len(word)] == word:
                for sentence in self.nextWord(s[len(word):], mem, dict):
                    if sentence: res.append(word + ' ' + sentence)
                    else: res.append(word)
        
        mem[s] = res
        return res
                    
                    
                    
    #     3. 正常dfs，并不能过
        
    #     return self.nextWord(s, {}, wordDict)
        
    # def nextWord(self, s, m, dict):
    #     if not s: return [None]
        
        
    #     res = []
    #     for word in dict:
    #         if s[:len(word)] == word:
    #             for sentence in self.nextWord(s[len(word):], m, dict):
    #                 if sentence: res.append(word + ' ' + sentence)
    #                 else: res.append(word)
        
        
    #     return res