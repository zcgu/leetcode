class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words: return ['']
        
    
        res = []
        p = 0
    
        while p < len(words):
            start = p
            l = len(words[p])
            p += 1
            while p < len(words) and l + 1 + len(words[p]) <= maxWidth:
                l = l + 1 + len(words[p])
                p += 1
    
            if p - start == 1:
                res.append(words[start] + ' ' * (maxWidth - l))
                continue
            
            if p == len(words):
                s = ''
                for i in range(start, p):
                    s += words[i] + ' '
                s += ' ' * (maxWidth - len(s))
                res.append(s)
                continue
            
            s = ''
            extraSpace = (maxWidth - l) / (p - start - 1)
            extraNum = (maxWidth - l) % (p - start - 1)
    
            for i in range(extraNum):
                s += words[start + i] + ' ' + ' ' * extraSpace + ' '
            
            for i in range(extraNum, p - start - 1):
                s += words[start + i] + ' ' + ' ' * extraSpace
            
            s += words[p - 1]
            
            res.append(s)
    
    	return res
    
# class Solution(object):
#     def fullJustify(self, words, maxWidth):
#         """
#         :type words: List[str]
#         :type maxWidth: int
#         :rtype: List[str]
#         """
#         if not words: return ['']
        
#         p1 = p2 = 0
#         res = []
        
#         while p2 < len(words):
#             length = len(words[p1])
#             p2 += 1
            
#             while p2 < len(words) and length + len(words[p2]) + 1 <= maxWidth:
#                 length += len(words[p2]) + 1
#                 p2 += 1
            
#             lst = words[p1:p2]
#             if p2 < len(words):
#                 extraSpaceLen = (maxWidth - length) / (p2 - p1- 1) if p2 - p1 != 1 else (maxWidth - length)
#                 extraNum = (maxWidth - length) % (p2 - p1- 1) if p2 - p1 != 1 else 0
                
#                 s = lst[0]
#                 i = 1
#                 for _ in range(extraNum):
#                     s += ' ' + ' ' * (extraSpaceLen + 1)
#                     s += lst[i]
#                     i += 1
#                 while i < len(lst):
#                     s += ' ' + ' ' * (extraSpaceLen)
#                     s += lst[i]
#                     i += 1
#                 s += ' ' * (maxWidth - len(s))
#             else:
#                 s = ' '.join(lst)
#                 s += ' ' * (maxWidth - len(s))
            
#             res.append(s)
#             p1 = p2
        
#         return res
