class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        p = 0
        while p < len(s):
            if s[p].isdigit():
                start = p
                while p < len(s) and s[p].isdigit():
                    p += 1
                stack.append(int(s[start:p]))
            elif s[p] == '[':
                stack.append('[')
                p += 1
            elif s[p] == ']':
                self.helper(stack)
                p += 1
            else:
                start = p
                while p < len(s) and s[p].isalpha():
                    p += 1
                stack.append(s[start:p])
        return ''.join(stack)
    
    def helper(self, stack):
        elem = stack.pop()
        s = ''
        while elem != '[':
            s = elem + s
            elem = stack.pop()
        
        num = stack.pop()
        stack.append(s * num)
        
        
        
        
#         if not s:
#             return ""
            
#         res = ""
        
#         i = 0
#         while i < len(s):
#             while not s[i].isdigit():
#                 res += s[i]
#                 i += 1
#                 if i >= len(s):
#                     return res
            
#             dstart = i
#             while s[i].isdigit():
#                 i += 1
                
#             digit = int(s[dstart: i])
            
#             start2 = i
#             count = 1
#             i += 1
#             while count > 0:
#                 if s[i] == '[':
#                     count += 1
#                 elif s[i] == ']':
#                     count -= 1
#                 i += 1
            
#             substr = self.decodeString(s[start2+1: i-1])
            
#             for _ in range(digit):
#                 res += substr
#         return res
