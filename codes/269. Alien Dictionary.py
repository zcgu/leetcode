class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = {}
        
        for word in words:
            for c in word:
                graph[c] = set()
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            for p, c in enumerate(word1):
                if p >= len(word2):
                    return ''
                    
                if word1[p] != word2[p]:
                    graph[word2[p]].add(word1[p])
                    break
        
        degree = {key: 0 for key in graph}
        for key in graph:
            for n in graph[key]:
                degree[n] += 1
        
        que = [key for key in degree if degree[key] == 0]
        res = ''
        
        while que:
            key = que.pop(0)
            res = key + res
            
            for n in graph[key]:
                degree[n] -= 1
                if degree[n] == 0:
                    que.append(n)
        
        if len(res) != len(graph):
            return ''
        else:
            return res
        
