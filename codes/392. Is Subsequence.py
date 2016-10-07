class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
            
        
        p1 = p2 = 0
        
        while p1 < len(s) and p2 < len(t):
            if t[p2] == s[p1]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        
        if p1 < len(s):
            return False
        else:
            return True

# # follow up, 很多s，一个t。把t创建map，值为每个字母的位置list。

#         table = {}
#         for i in range(len(t)):
#             table[t[i]] = table[t[i]] + [i] if t[i] in table else [i]
        
#         p = -1
#         for c in s:
#             if c not in table: return False
            
#             index = self.bs(table[c], p)
            
#             if index >= len(table[c]): return False
            
#             p = table[c][index]
        
#         return True
    
#     def bs(self, lst, num):
#         left = 0
#         right = len(lst)
        
#         while left < right:
#             mid = (left + right) / 2
            
#             if lst[mid] == num:
#                 left = mid + 1
#             elif lst[mid] < num:
#                 left = mid + 1
#             else:
#                 right = mid
        
#         return left
        
        
        
        
        
        