class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lst = []
        
        for word in words:
            tmp = 0
            for c in word:
                tmp |= (1 << (ord(c) - ord('a')))
            lst.append(tmp)
            
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if lst[i] & lst[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
        