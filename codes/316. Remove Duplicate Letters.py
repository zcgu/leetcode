class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = {c: s.count(c) for c in set(s)}
        
        stack = []
        
        for c in s:
            if c in stack:
                table[c] -= 1
                continue
            
            while stack and stack[-1] > c and table[stack[-1]] > 0:
                stack.pop()
            
            table[c] -= 1
            stack.append(c)
        
        return ''.join(stack)

# class Solution(object):
#     def removeDuplicateLetters(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         table = {chr(ord('a') + i): s.count(chr(ord('a') + i)) for i in range(26)}

#         visit = [False for _ in range(26)]
        
#         stack = []
        
#         for c in s:
#             table[c] -= 1
            
#             if visit[ord(c) - ord('a')]:
#                 continue
            
#             while stack and stack[-1] > c and table[stack[-1]] > 0:
#                 visit[ord(stack[-1]) - ord('a')] = False
#                 stack.pop()
                
#             visit[ord(c) - ord('a')] = True
#             stack.append(c)
        
#         return ''.join(stack)
        
        
        
        
        # 1. greedy
        # for c in sorted(set(s)):
        #     suffix = s[s.index(c):]
        #     if set(suffix) == set(s):
        #         suffix = suffix.replace(c, '')
        #         return c + self.removeDuplicateLetters(suffix)
        # return ''
