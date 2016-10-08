class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPali(word):
            # p1 = 0
            # p2 = len(word) - 1
            # while p1 < p2:
            #     if word[p1] != word[p2]: return False
            #     p1 += 1
            #     p2 -=1
            # return True
            return word == word[::-1]
        
        table = {}
        res = set()
        
        for i, word in enumerate(words):
            table[word] = i
        
        for i, word in enumerate(words):
            for pos in range(len(word) + 1):
                first = word[:pos]
                second = word[pos:]
                
                if isPali(first) and second[::-1] in table and i != table[second[::-1]]:
                    res.add((table[second[::-1]], i))
                if isPali(second) and first[::-1] in table and i != table[first[::-1]]:
                    res.add((i, table[first[::-1]]))
                    
        return list(res)
            
            