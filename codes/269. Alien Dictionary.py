# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# For example,
# Given the following words in dictionary,

# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".

# Note:
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # 拓扑排序

        total = set()
        for word in words:
            for c in word:
                total.add(c)
        
        graph = {c: set() for c in total}

        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
     
            p1 = p2 = 0
            
            while p1 < len(word1) and p2 < len(word2) and word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
            
            if p1 < len(word1) and p2 >= len(word2):
                return ''
                
            if p1 >= len(word1) or p2 >= len(word2):
                continue
            
            graph[word1[p1]].add(word2[p2])
        
        res = ''
        que = []
        degree = {c: 0 for c in total}
        
        for c in graph:
            degree[c] = len(graph[c])
            if len(graph[c]) == 0:
                que.append(c)
                
        while que:
            c = que.pop(0)
            res = c + res
            
            for p in graph:
                if c in graph[p]:
                    degree[p] -= 1
                    
                    if degree[p] == 0:
                        que.append(p)
        
        if max(degree.values()) > 0:
            return ''

        return res
        
        
        
        
