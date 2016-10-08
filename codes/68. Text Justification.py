class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words: return ['']
        
        p1 = p2 = 0
        res = []
        
        while p2 < len(words):
            length = len(words[p1])
            p2 += 1
            
            while p2 < len(words) and length + len(words[p2]) + 1 <= maxWidth:
                length += len(words[p2]) + 1
                p2 += 1
            
            lst = words[p1:p2]
            if p2 < len(words):
                extraSpaceLen = (maxWidth - length) / (p2 - p1- 1) if p2 - p1 != 1 else (maxWidth - length)
                extraNum = (maxWidth - length) % (p2 - p1- 1) if p2 - p1 != 1 else 0
                
                s = lst[0]
                i = 1
                for _ in range(extraNum):
                    s += ' ' + ' ' * (extraSpaceLen + 1)
                    s += lst[i]
                    i += 1
                while i < len(lst):
                    s += ' ' + ' ' * (extraSpaceLen)
                    s += lst[i]
                    i += 1
                s += ' ' * (maxWidth - len(s))
            else:
                s = ' '.join(lst)
                s += ' ' * (maxWidth - len(s))
            
            res.append(s)
            p1 = p2
        
        return res
                
                
                